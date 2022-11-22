terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-2"
}

resource "aws_instance" "inst" {
  ami               = "ami-031dea1a744251b51"
  availability_zone = "us-east-2a"

  instance_type = "t4g.nano"

  tags = {
    Name = "data_backup"
  }
}

resource "aws_ebs_volume" "data-volume" {
  availability_zone = "us-east-2a"
  size              = 125

  tags = {
    Name = "data_backup"
  }
}

resource "aws_volume_attachment" "volume" {
  device_name = "/dev/sdc"
  volume_id   = aws_ebs_volume.data-volume.id
  instance_id = aws_instance.inst.id
}