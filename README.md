# Backup Data
Backup data from websites such as Facebook or Google Takeout. This can be extremely useful if you have a data cap from your ISP, but still wish to backup your data.

Steps to use:
1. Wait for Google Takeout or Facebook Downloads to finish processing
1. \* [Create the aws instance](./docs/aws_instance.md)
1. \* [Initialize the hard drive](./docs/initialize_hdd.md)
1. \*\* [Import your GPG public key into the new ec2 virtual machine](./docs/gpg.md)
1. [Get the download link for each file you wish to download](./docs/download_link.md)
1. Using the links found in the previous step, [create the required text file](./docs/create_required_txt_file.md)
1. Do the same for all services you wish to back up
1. [Run the script](./docs/run_the_script.md)
1. Destroy or shut down the instance

\* Can be skipped if starting from a previously shutdown ec3 instance

\*\* Skip this step and leave out the email parameter when running the script to avoid encryption before uploading

That's it! The script will go through all txt files and download each url to your Deep Archive S3 bucket

Taken and edited from https://gunargessner.com/takeout
