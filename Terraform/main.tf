
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}
provider "aws" {
  region = "ap-southeast-2"
}
#######################
# Create instance ec2 #
#######################

resource "aws_instance" "ec2_instance" {
  ami             = "ami-0f5d1713c9af4fe30"
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.instances.name]
  user_data = "${file("/Users/gabrielparedes/Documents/gp/odoo/Terraform/deploy.sh")}"
  ebs_block_device {
    device_name = "/dev/sda1"
    volume_size = 20
  }
}

#Create elastic ip
resource "aws_eip" "eip"{
vpc = true
instance= aws_instance.ec2_instance.id
}

data "aws_vpc" "default_vpc" {
  default = true
}

data "aws_subnet_ids" "default_subnet" {
  vpc_id = data.aws_vpc.default_vpc.id
}

resource "aws_security_group" "instances" {
  name = "instance-security-group"
}

resource "aws_security_group_rule" "allow_http_inbound" {
  type              = "ingress"
  security_group_id = aws_security_group.instances.id
  from_port   = 80
  to_port     = 80
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}

resource "aws_security_group_rule" "allow_odoo_http_inbound" {
  type              = "ingress"
  security_group_id = aws_security_group.instances.id
  from_port   = 8069
  to_port     = 8069
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}

resource "aws_security_group_rule" "allow_https_inbound" {
  type              = "ingress"
  security_group_id = aws_security_group.instances.id
  from_port   = 443
  to_port     = 443
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}

resource "aws_security_group_rule" "allow_ssh_inbound" {
  type              = "ingress"
  security_group_id = aws_security_group.instances.id
  from_port   = 22
  to_port     = 22
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}

resource "aws_security_group_rule" "allow_nginx_inbound" {
  type              = "ingress"
  security_group_id = aws_security_group.instances.id

  from_port   = 81
  to_port     = 81
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}

resource "aws_security_group_rule" "allow_outbound" {
  type              = "egress"
  security_group_id = aws_security_group.instances.id
  from_port   = 0
  to_port     = 0
  protocol    = "-1"
  cidr_blocks = ["0.0.0.0/0"]

}

#####################
# Route53 AJFencing #
#####################

resource "aws_route53_zone" "ajfencing_primary" {
  name = "ajfencing.com.au"
}

resource "aws_route53_record" "ajfencing_root" {
  zone_id = aws_route53_zone.ajfencing_primary.zone_id
  name    = "ajfencing.com.au"
  type    = "A"
  ttl     = "300"
  records = [aws_instance.ec2_instance.public_ip]
}
resource "aws_route53_record" "ajfencing_www" {
  zone_id = aws_route53_zone.ajfencing_primary.zone_id
  name    = "www.ajfencing.com.au"
  type    = "A"
  ttl     = "300"
  records = [aws_instance.ec2_instance.public_ip]
}
resource "aws_route53_record" "ajfencing_test" {
  zone_id = aws_route53_zone.ajfencing_primary.zone_id
  name    = "test.ajfencing.com.au"
  type    = "A"
  ttl     = "300"
  records = [aws_instance.ec2_instance.public_ip]
}