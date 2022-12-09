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

  provisioner "file" {
    source      = "../backup.py"
    destination = "/home/ec2-user/backup.py"
  }

  provisioner "file" {
    source      = "./data/import.gpg"
    destination = "/home/ec2-user/import.gpg"
  }

  provisioner "file" {
    source      = "./data/data.json"
    destination = "/home/ec2-user/data.json"
  }

  provisioner "file" {
    source      = "./data/mount_hdd.sh"
    destination = "/home/ec2-user/mount_hdd.sh"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo gpg --import import.gpg"
    ]
  }
  
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/aws_key")
    host        = self.public_ip
  }

  vpc_security_group_ids = [aws_security_group.main.id]
  key_name = "${aws_key_pair.deployer.id}"

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


resource "aws_security_group" "main" {
  egress = [
    {
      cidr_blocks      = [ "0.0.0.0/0", ]
      description      = ""
      from_port        = 0
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      protocol         = "-1"
      security_groups  = []
      self             = false
      to_port          = 0
    }
  ]
 ingress                = [
   {
     cidr_blocks      = [ "0.0.0.0/0", ]
     description      = ""
     from_port        = 22
     ipv6_cidr_blocks = []
     prefix_list_ids  = []
     protocol         = "tcp"
     security_groups  = []
     self             = false
     to_port          = 22
  }
  ]
}

resource "aws_key_pair" "deployer" {
  key_name   = "aws_key"
  public_key = file("~/.ssh/aws_key.pub")
}
