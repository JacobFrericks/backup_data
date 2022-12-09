## Create SSH keys
1. run `ssh-keygen`
1. Save SSH keys under `~/.ssh/aws_key`

# Run Terraform
1. Download and install Terraform
1. Authenticate with AWS as described [here](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#authentication-and-configuration)
1. Cd into the tf directory: `cd tf`
1. Run `terraform apply`
1. Copy the public_dns that is in the outputs after the apply finishes

## SSH into instance and run the script
1. Run `ssh -i ~/.ssh/aws_key ec2-user@<public_dns>` where you paste in the public_dns
1. On the instance, run `python3 backup.py`

## Destroy instances
1. When finished, run `terraform destroy`