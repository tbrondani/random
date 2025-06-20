#!/bin/bash
##Create or Destroy a Prowler User/Role
## TLDR fetches the github repo from prowler and create a user or role 
## If you need other service instead of EC2 edit the trustpolicy.
## I dont own prowler , this is just a way to make your life easier!

ROLE_NAME="ProwlerRole"
POLICY_NAME="ProwlerAdditionsPolicy"
TRUST_POLICY_FILE="trust-policy.json"
CUSTOM_POLICY_FILE="prowler-policy.json"
USER_NAME="ProwlerUser"

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text --no-cli-pager)
POLICY_ARN="arn:aws:iam::$ACCOUNT_ID:policy/$POLICY_NAME"

createrole() {
  echo "[+] Downloading policy from GitHub..."
  curl -s -o "$CUSTOM_POLICY_FILE" https://raw.githubusercontent.com/prowler-cloud/prowler/master/permissions/prowler-additions-policy.json

  echo "[+] Creating custom IAM policy..."
  aws iam create-policy \
    --policy-name "$POLICY_NAME" \
    --policy-document file://"$CUSTOM_POLICY_FILE" \
    --no-cli-pager

  echo "[+] Creating trust policy for anyone in the account..."
  cat > "$TRUST_POLICY_FILE" <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::$ACCOUNT_ID:root"
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

  echo "[+] Attaching policies to role..."
  aws iam attach-role-policy --role-name "$ROLE_NAME" --policy-arn "$POLICY_ARN" --no-cli-pager
  aws iam attach-role-policy --role-name "$ROLE_NAME" --policy-arn arn:aws:iam::aws:policy/SecurityAudit --no-cli-pager
  aws iam attach-role-policy --role-name "$ROLE_NAME" --policy-arn arn:aws:iam::aws:policy/job-function/ViewOnlyAccess --no-cli-pager

  echo "[*] Cleaning up temporary files..."
  rm -f "$CUSTOM_POLICY_FILE" "$TRUST_POLICY_FILE"

  echo "[✓] Role creation completed!"
}

destroyrole() {
  echo "[!] Deleting IAM role (ignoring errors)..."
  aws iam delete-role --role-name "$ROLE_NAME" --no-cli-pager 2>/dev/null
  deletepolicy
  echo "[✓] Role deletion completed!"
}

createuser() {
  echo "[+] Creating IAM user: $USER_NAME..."
  aws iam create-user --user-name "$USER_NAME" --no-cli-pager

  echo "[+] Attaching policies to user..."
  aws iam attach-user-policy --user-name "$USER_NAME" --policy-arn "$POLICY_ARN" --no-cli-pager
  aws iam attach-user-policy --user-name "$USER_NAME" --policy-arn arn:aws:iam::aws:policy/SecurityAudit --no-cli-pager
  aws iam attach-user-policy --user-name "$USER_NAME" --policy-arn arn:aws:iam::aws:policy/job-function/ViewOnlyAccess --no-cli-pager

  echo "[✓] User created and policies attached!"
}

destroyuser() {
  echo "[!] Detaching policies from user (ignoring errors)..."
  aws iam detach-user-policy --user-name "$USER_NAME" --policy-arn "$POLICY_ARN" --no-cli-pager 2>/dev/null
  aws iam detach-user-policy --user-name "$USER_NAME" --policy-arn arn:aws:iam::aws:policy/SecurityAudit --no-cli-pager 2>/dev/null
  aws iam detach-user-policy --user-name "$USER_NAME" --policy-arn arn:aws:iam::aws:policy/job-function/ViewOnlyAccess --no-cli-pager 2>/dev/null

  echo "[!] Destroying IAM user: $USER_NAME..."
  aws iam delete-user --user-name "$USER_NAME" --no-cli-pager 2>/dev/null

  deletepolicy
  echo "[✓] User deletion completed!"
}

deletepolicy() {
  echo "[!] Deleting custom Prowler policy to avoid leaving unused stuff in the account (ignoring errors)..."
  aws iam delete-policy --policy-arn "$POLICY_ARN" --no-cli-pager 2>/dev/null
}


# Main command dispatcher
case "$1" in
  createrole)
    createrole
    ;;
  destroyrole)
    destroyrole
    ;;
  createuser)
    createuser
    ;;
  destroyuser)
    destroyuser
    ;;
  *)
    echo "Usage: $0 {createrole|destroyrole|createuser|destroyuser}"
    exit 1
    ;;
esac
