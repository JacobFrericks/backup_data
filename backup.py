# noqa: E111
import json
import sys
import os
from datetime import date


def validate_json(data):
  if not data.get("bucket_name"):
    print("No bucket name found!")
    sys.exit(1)
  return data

def get_encrypt_str(gpg_email, output_file_name):
  if not gpg_email:
    return ""
  return f"| gpg --encrypt -r {gpg_email} --trust-model always --output {output_file_name}"

def get_curl_str(encrypt_str, link, bucket_name, output_file_name):
  return f'curl {link} {encrypt_str} | aws s3 cp - "s3://{bucket_name}/{output_file_name}" --storage-class DEEP_ARCHIVE'

def save_files(type, fmt, download_links, gpg_email, bucket_name):
  cmd_used = ""
  for count, link in enumerate(download_links):
    file_name=f"{type}_{date.today()}_{count}.{fmt}"
    encryptStr = get_encrypt_str(gpg_email, file_name)
    curl_str = get_curl_str(encryptStr, link, bucket_name, file_name)
    os.system(curl_str)
    cmd_used = f"{cmd_used} && {curl_str}"
  return cmd_used[4:] # "4" removes the first " && " from the command str

def main():
  os.system("chmod +x ./mount_hdd.sh && sudo ./mount_hdd.sh")
  file = open("data.json")
  data = json.load(file)
  validate_json(data)

  cmd_str_google = save_files("google", data.get("google_fmt"), data.get("google_links"), data.get("gpg_email"), data.get("bucket_name"))
  cmd_str_facebook = save_files("facebook", data.get("facebook_fmt"), data.get("facebook_links"), data.get("gpg_email"), data.get("bucket_name"))
  return {
    "google": cmd_str_google, 
    "facebook": cmd_str_facebook
  }

if __name__ == "__main__":
  print(main())
