provider "aws" {
  region = "us-east-1"

  #   assume_role {
  #     role_arn = "arn:aws:iam::[AWS_ACCOUNT]:role/[IAM_ROLE_WITH_PERMISSION]"
  #   }

  default_tags {
    tags = {
      managed-by = "terraform"
      source     = "https://github.com/brunoevonah/fastapi-poc/terraform"
    }
  }
}

# Used for EKS access, can be changed to use kubeconfig as well.
# provider "kubernetes" {
#   host                   = var.cluster_endpoint
#   cluster_ca_certificate = base64decode(var.cluster_ca_cert)
#   exec {
#     api_version = "client.authentication.k8s.io/v1alpha1"
#     args        = ["eks", "get-token", "--cluster-name", var.cluster_name]
#     command     = "aws"
#   }
# }

# Used for direct kubeconfig

# provider "kubernetes" {
#   config_path = "~/.kube/config"
# }
