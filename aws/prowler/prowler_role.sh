#!/bin/bash
##Create or Destroy a Prolwer Custom Role
## If you need other service instead of EC2 edit the trustpolicy.
# I dont own prowler , this is just a way to make your life easier!

ROLE_NAME="ProwlerRole"
POLICY_NAME="ProwlerCustomPolicy"
TRUST_POLICY_FILE="trust-policy.json"
CUSTOM_POLICY_FILE="prowler-policy.json"

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text --no-cli-pager)
POLICY_ARN="arn:aws:iam::$ACCOUNT_ID:policy/$POLICY_NAME"

create() {
  echo "[+] Downloading policy from GitHub..."
  curl -s -o "$CUSTOM_POLICY_FILE" https://raw.githubusercontent.com/prowler-cloud/prowler/master/permissions/prowler-additions-policy.json

  echo "[+] Creating custom IAM policy..."
  aws iam create-policy \
    --policy-name "$POLICY_NAME" \
    --policy-document file://"$CUSTOM_POLICY_FILE" \
    --no-cli-pager

  echo "[+] Creating trust policy for EC2 service..."
  cat > "$TRUST_POLICY_FILE" <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

  echo "[+] Creating IAM role $ROLE_NAME..."
  aws iam create-role \
    --role-name "$ROLE_NAME" \
    --assume-role-policy-document file://"$TRUST_POLICY_FILE" \
    --no-cli-pager

  echo "[+] Attaching policies..."
  aws iam attach-role-policy --role-name "$ROLE_NAME" --policy-arn "$POLICY_ARN" --no-cli-pager
  aws iam attach-role-policy --role-name "$ROLE_NAME" --policy-arn arn:aws:iam::aws:policy/SecurityAudit --no-cli-pager
  aws iam attach-role-policy --role-name "$ROLE_NAME" --policy-arn arn:aws:iam::aws:policy/job-function/ViewOnlyAccess --no-cli-pager

  echo "[*] Cleaning up temporary files..."
  rm -f "$CUSTOM_POLICY_FILE" "$TRUST_POLICY_FILE"

  echo "[✓] Creation completed successfully!"
}

destroy() {
  echo "[!] Forcing deletion of IAM role and policy (ignoring errors)..."

  aws iam delete-role --role-name "$ROLE_NAME" --no-cli-pager 2>/dev/null
  aws iam delete-policy --policy-arn "$POLICY_ARN" --no-cli-pager 2>/dev/null

  echo "[✓] Destruction completed!"
}

# Main entry point
case "$1" in
  create)
    create
    ;;
  destroy)
    destroy
    ;;
  *)
    echo "Usage: $0 {create|destroy}"
    exit 1
    ;;
esac
