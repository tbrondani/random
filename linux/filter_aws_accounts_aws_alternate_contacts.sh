### Run a assesment using the list option in https://github.com/aws-samples/aws-organizations-alternate-contact-manager
##  export the JSON to a bucket s3, using the LIST option.

# For Billing Lists
cat list.json | jq '.AlternateContact | to_entries[] | select(.value.Billing == "Null") | .key' | tr '\n' ',' | sed s/\"//g > super.txt

# For Security Lists
cat list.json | jq '.AlternateContact | to_entries[] | select(.value.Security == "Null") | .key' | tr '\n' ',' | sed s/\"//g > super.txt

#This will generate a oneliner in the following format to be applied later using the UPDATE option in the aws-organizations-alternate-contact-manager.

' 000000000001,000000000002,000000000003,000000000004.'

# This will be used to alter or modify the contacts.
