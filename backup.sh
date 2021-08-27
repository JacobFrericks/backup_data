##!/usr/bin/env bash

## XXX: Set your bucket name here
AWS_S3_BUCKET="Backup"

## XXX: Set your gpg encryption email address here (or remove the `gpg` line)
GPG_EMAIL=""

## Gets last argument
filename=$1

## Gets all but the last 3 arguments
site=$2

echo "Downloading: $filename"

## Expands all args (i.e. `args[@]`) in a format that can be reused as input (i.e. `@Q`)
cat *.txt >> all.txt
while read url; do
  curl $url \
    | gpg --encrypt -r ${GPG_EMAIL} --trust-model always --output ${url}.txt #\
    | aws s3 cp - "s3://${AWS_S3_BUCKET}/${filename}" \
        --storage-class DEEP_ARCHIVE 
done <all.txt
rm -rf all.txt
