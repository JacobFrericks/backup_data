## Creating the EC2 instance
1. Spin up an ec2 instance AWS in a region somewhere with cheap storage, like US-East (Ohio)
1. Choose `Amazon Linux 2 AMI` with `64-bit (ARM)`
1. Use a t4g.nano
1. Click `Next: Configure Instance Details`
1. Go to `Add Storage`, and click `Add New Volume`
1. Under `Volume Type`, choose `Cold HDD` (This is the slowest, but cheapest hard drive for storage)
1. Keep the size at the lowest size available: `125GB`
1. Check `Delete on Termination`
1. Click `Review and Launch`

## Create the bucket
1. Go to the S3 page
1. Create a bucket
1. Remember the name of the bucket