terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

variable "db_password" {
  type      = string
  sensitive = true
  default   = "change-me-in-real-life"
}

# Compute
resource "aws_instance" "web" {
  ami           = "ami-0abcd1234efgh5678"
  instance_type = "t3.micro"

  tags = {
    Name = "web"
  }
}

resource "aws_instance" "batch_worker" {
  ami           = "ami-0abcd1234efgh5678"
  instance_type = "m5.4xlarge"

  tags = {
    Name = "batch-worker"
  }
}

# Managed database
resource "aws_db_instance" "primary" {
  allocated_storage   = 100
  engine              = "postgres"
  engine_version      = "15.3"
  instance_class      = "db.t3.medium"
  db_name             = "appdb"
  username            = "app"
  password            = var.db_password
  skip_final_snapshot = true
}

# Storage
resource "aws_ebs_volume" "data" {
  availability_zone = "us-east-1a"
  size              = 500
  type              = "gp3"
}

resource "aws_s3_bucket" "assets" {
  bucket = "lornets-example-assets-bucket"
}

# Network
resource "aws_nat_gateway" "egress" {
  allocation_id = "eipalloc-0123456789abcdef0"
  subnet_id     = "subnet-0123456789abcdef0"
}
