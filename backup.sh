##!/usr/bin/env bashm

AWS_S3_BUCKET="Backup"

GPG_EMAIL=$1
if [ -z "$GPG_EMAIL" ]; then
  CURL_CMD="curl \${line} \
      | aws s3 cp - \"s3://\${AWS_S3_BUCKET}/\${filename}\" \
        --storage-class DEEP_ARCHIVE"
else
  CURL_CMD="curl \${line} \
      | gpg --encrypt -r \${GPG_EMAIL} --trust-model always --output \${filename} \
      | aws s3 cp - \"s3://\${AWS_S3_BUCKET}/\${filename}\" \
        --storage-class DEEP_ARCHIVE"
fi

for file in *.txt; do
  echo "### $file ###"
  count=0
  while read line; do
    if [ "$count" -eq "0" ]; then
      extension=${line}
      count=$((count+1))
      continue
    fi
    filename=${file%.*}_${count}.${extension}
    echo "Downloading: $filename"
    eval $CURL_CMD
    count=$((count+1))
  done <${file}
done
