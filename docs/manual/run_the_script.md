## Running the script
You can run the script one of two ways. You can either copy/paste the script into your folder and run it from there, or you can run it on demand.

### Copy/Paste
1. Visit https://github.com/JacobFrericks/backup_data/blob/main/backup.py and copy the script
1. Create a new file named `backup.py` on your EC2 instance
1. Paste the script in the file
1. Create and fill out data.json
1. Run the script: `python3 backup.py`

### Run the script
1. Run the script: `python3 <(curl -s https://raw.githubusercontent.com/JacobFrericks/backup_data/main/backup.py)`