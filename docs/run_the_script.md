## Running the script
You can run the script one of two ways. You can either copy/paste the script into your folder and run it from there, or you can run it as a bash download.

### Copy/Paste
1. Visit https://github.com/JacobFrericks/backup_data/blob/main/backup.sh and copy the script
1. Create a new file named `backup.sh` on your EC2 instance
1. Paste the script in the file
1. Run the following command: `chmod +x backup.sh`
1. Run the script: `./backup.sh $my_bucket_name $my_email`

### Bash Download
1. Run the script: `bash <(curl -s https://raw.githubusercontent.com/JacobFrericks/backup_data/main/backup.sh) $my_bucket_name $my_email`

NOTE: You can leave out the email parameter if you do not wish to have your files encrypted before uploading