terraform {
  required_version = ">= 1"

required_providers {
  aws = {
    source = "hashicorp/aws"
    version = ">=4"
  }
}
}

resource "aws_secretsmanager_secret" "random" {
  name = "super-secret-classified"
  description = "something secret"
  recovery_window_in_days = 0
  force_overwrite_replica_secret = true
}