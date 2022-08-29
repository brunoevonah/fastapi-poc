terraform {

  # To use s3 as a shared backend
  #   backend "s3" {
  #     bucket         = "tf-statelock"
  #     key            = "tf-statelock/fastapipoc/terraform.tfstate"
  #     dynamodb_table = "tf-statelock"
  #     region         = "us-east-1"
  #     encrypt        = true
  #     role_arn       = "arn:aws:iam::[AWS_ACCOUNT]:role/[IAM_ROLE_WITH_PERMISSION]"
  #   }

  # Terraform Version
  required_version = ">= 1.2.8"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.8.0"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.13.1"
    }

  }

}
