# Backup Data
Backup data from websites such as Facebook or Google Takeout

First time use:
1. Wait for Google Takeout or Facebook Downloads to finish processing
1. \* Spin up an ec2 instance AWS in a region somewhere with cheap storage, like US-East (Ohio)
1. \* \*\* Import your GPG public key into the new ec2 virtual machine
1. \* Create a Glacier bucket called "backup"
1. From a computer, with Firefox, click to download each of the files, and then cancel all of the downloads.
1. In Firefox, go to the downloads manager, and for each cancelled download, right click, then choose “Copy Download Link”.
1. Copy the link to the AWS EC2 instance, in a file ending in ".txt", such as "google.txt". The first line in this file MUST be the extension used. ie "zip"
1. Add an empty line at the end of each *.txt files (see `example.txt` for an example of what these files should look like)
1. Do the same for all services you wish to back up
1. Run this script in the same directory as your text files using your gpg email address as the only parameter (ie `$backup.sh myemail@gmail.com`) NOTE: If you skip this parameter, your files will simply not be encrypted
1. Destroy or shut down the instance

\* Can be skipped if starting from a previously shutdown ec3 instance

\** Skip this step and leave out the email parameter when running the script to avoid encryption before uploading

That's it! The script will go through all txt files and download each url to your Glacier vault bucket

Taken and edited from https://gunargessner.com/takeout
