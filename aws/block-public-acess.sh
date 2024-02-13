#!/bin/bash

echo "Select an action below - please refer to my article for more info."
echo "If you find this script helpful
echo "consider buying me a coffee: https://www.buymeacoffee.com/tbrondani""

PS3="Select a number from 1 to 3 or press 'q' to quit:"

options=(" Get the current state of config " " Apply restrictions to EC2 and S3 public" " Disable the blocks and private configs" " Press "q" to Quit")

select option in "${options[@]}"
do
    case $REPLY in
        1)
            echo "Reading the states of every block"
            echo "## EBS Encryption ##"
            aws ec2 get-ebs-encryption-by-default
            echo "## Snapshot public access state ##"
            aws ec2 get-snapshot-block-public-access-state
            echo "## AMI public access state ## "
            aws ec2 get-image-block-public-access-state
            echo "## S3 Public block state ##"
            ID=$(aws sts get-caller-identity --query "Account" --output text) ; aws s3control get-public-access-block --account-id ${ID}
            break
            ;;
        2)
            echo "Applying the block"
            read -p "Are you sure? (y/n): " confirm
            if [[ $confirm == [yY] ]]; then
                aws ec2 enable-ebs-encryption-by-default ; echo "## EBS Encryption ENABLED"
                aws ec2 enable-snapshot-block-public-access --state block-all-sharing ; echo " ## Snapshot public access BLOCKED"
                aws ec2 enable-image-block-public-access --image-block-public-access-state block-new-sharing ; echo " ## AMI public access BLOCKED"
                ID=$(aws sts get-caller-identity --query "Account" --output text) ; aws s3control put-public-access-block --public-access-block-configuration '{"BlockPublicAcls": true, "IgnorePublicAcls": true, "BlockPublicPolicy": true, "RestrictPublicBuckets": true}' --account-id ${ID} ; aws s3control get-public-access-block --account-id ${ID} ; echo "## S3 Public block ENABLED  ##"
                echo "$option DONE!"
                break
            else
                echo "Changes not applied."
            fi
            ;;
        3)
            echo "Disabling blocks"
            read -p "You sure that you want to disable and rollback changes? (y/n): " confirm
            if [[ $confirm == [yY] ]]; then
                aws ec2 disable-ebs-encryption-by-default ; echo "## EBS Encryption DISABLED"
                aws ec2 disable-snapshot-block-public-access ; echo " ## Snapshot public access UNRESTRICTED"
                aws ec2 disable-image-block-public-access ; echo " ## AMI public access UNRESTRICTED"
                ID=$(aws sts get-caller-identity --query "Account" --output text) ; aws s3control put-public-access-block --public-access-block-configuration '{"BlockPublicAcls": false, "IgnorePublicAcls": false, "BlockPublicPolicy": false, "RestrictPublicBuckets": false}' --account-id ${ID} ; aws s3control get-public-access-block --account-id ${ID} ; echo "## S3 Public block UNRESTRICTED"
                echo "$option DONE!"
                break
            else
                echo "Changes not rolled back, everything stays the same!"
            fi
            ;;
        [Qq])
            echo "Bye and thanks for the fish! If you enjoyed this script, consider buying me a coffee: https://www.buymeacoffee.com/tbrondani"
            break
            ;;

        *)
            echo "Ooops - unknown choice $REPLY, hit 'q' if you want to leave the script ";;
    esac
done

