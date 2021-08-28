##!/usr/bin/env bashm

## XXX: Set your bucket name here
AWS_S3_BUCKET="Backup"

## XXX: Set your gpg encryption email address here (or remove the `gpg` line)
GPG_EMAIL=$1

## Expands all args (i.e. `args[@]`) in a format that can be reused as input (i.e. `@Q`)
for file in *.txt; do
  echo "### $file ###"
  count=0
  extension=""
  while read line; do
    if [ "$count" -eq "0" ]; then
      extension=${line}
      count=$((count+1))
      continue
    fi
    filename=${file%.*}_${count}.${extension}
    echo "Downloading: $filename"
    curl ${line} \
      | gpg --encrypt -r ${GPG_EMAIL} --trust-model always --output $filename \
      | aws s3 cp - "s3://${AWS_S3_BUCKET}/${filename}" \
        --storage-class DEEP_ARCHIVE
    count=$((count+1))
  done <${file}
done

#while read line; do
#  # if GPG email is not empty
#    # cmd="gpg --encrypt -r ${GPG_EMAIL} --trust-model always --output ${line}.txt"
#  curl $line \
#    | gpg --encrypt -r ${GPG_EMAIL} --trust-model always --output ${line}.txt #\
#    | aws s3 cp - "s3://${AWS_S3_BUCKET}/${filename}" \
#        --storage-class DEEP_ARCHIVE
#done <all.txt
#rm -rf all.txt
