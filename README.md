# Backup Data
Backup data from websites such as Facebook or Google Takeout. This can be extremely useful if you have a data cap from your ISP, but still wish to backup your data.

## Easy/Automatic (using Terraform)
1. Wait for Google Takeout or Facebook Downloads to finish processing
1. \*\* [Create your GPG public key](./docs/automatic/gpg.md)
1. [Get the download link for each file you wish to download](./docs/download_link.md)
1. [Create the required json file](./docs/create_required_data_file.md). Save the json in `tf/data/data.json`
1. Follow the steps in [the terraform doc](./docs/automatic/terraform.md)

\*\* Skip this step and leave the `gpg_email` value blank when running the script to avoid encryption before uploading

## Hard/Manual
Steps to use:
1. Wait for Google Takeout or Facebook Downloads to finish processing
1. \* [Create the aws instance](./docs/manual/aws_instance.md)
1. \* [Initialize the hard drive](./docs/manual/initialize_hdd.md)
1. \*\* [Create and import your GPG public key into the new ec2 virtual machine](./docs/manual/gpg.md)
1. [Get the download link for each file you wish to download](./docs/download_link.md)
1. Using the links found in the previous step, [create the required json file](./docs/create_required_data_file.md)
1. [Run the script](./docs/manual/run_the_script.md)
1. Destroy or shut down the instance

\* Can be skipped if starting from a previously shutdown ec3 instance

\*\* Skip this step and leave the `gpg_email` value blank when running the script to avoid encryption before uploading

That's it! The script will go through all links and download the file to your Deep Archive S3 bucket

Taken and edited from https://gunargessner.com/takeout
