# noqa: E111
import json
import sys
import os
from datetime import date
import concurrent.futures
import time
import logging


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

def save_file(curl_str):
  os.system(curl_str)

def save_files(type, fmt, download_links, gpg_email, bucket_name):
  cmds_to_run = []
  for count, link in enumerate(download_links):
    file_name = f"{type}_{date.today()}_{count}.{fmt}"
    encryptStr = get_encrypt_str(gpg_email, file_name)
    curl_str = get_curl_str(encryptStr, link, bucket_name, file_name)
    cmds_to_run.append(curl_str)
  return cmds_to_run

def main():
  mnt_hdd = "mount_hdd.sh"
  if os.path.isfile(mnt_hdd):
    os.system(f"chmod +x {mnt_hdd} && sudo {mnt_hdd}")
  
  file = open("data.json")
  data = json.load(file)
  validate_json(data)

  cmds_to_run = []

  cmd_google = save_files("google", data.get("google_fmt"), data.get("google_links"), data.get("gpg_email"), data.get("bucket_name"))
  cmds_to_run.extend(cmd_google)

  cmd_facebook = save_files("facebook", data.get("facebook_fmt"), data.get("facebook_links"), data.get("gpg_email"), data.get("bucket_name"))
  cmds_to_run.extend(cmd_facebook)

  with concurrent.futures.ThreadPoolExecutor() as executor:
    [executor.submit(save_file, param) for param in cmds_to_run]

  return {
    "google": cmd_google, 
    "facebook": cmd_facebook
  }

if __name__ == "__main__":
  
  format = "%(asctime)s: %(message)s"
  logging.basicConfig(format=format, level=logging.INFO,
                      datefmt="%H:%M:%S")
  print(main())
