### Run a assesment using the list option in https://github.com/aws-samples/aws-organizations-alternate-contact-manager
##  export the JSON to a bucket s3, using the LIST option.
## there are 2 commands because there is difference of CRLF and LF in the files when they are generated in windows or linux
## dos2unix could help here but I found it easier to just add a tr in the oneliner :)

###### Linux running on WSL or Windows Bash
cat list.json | jq '.AlternateContact | to_entries[] | select(.value.Billing == "Null") | .key' | tr '\n' ','| tr -d '\r' | sed 's/\"//g ; $s/,$//' > list.txt

###### Pure linux
# For Billing Lists
cat list.json | jq '.AlternateContact | to_entries[] | select(.value.Billing == "Null") | .key' | tr '\n' ',' | sed 's/\"//g ; $s/,$//' > list.txt

# For Security Lists
cat list.json | jq '.AlternateContact | to_entries[] | select(.value.Security == "Null") | .key' | tr '\n' ',' | sed 's/\"//g ; $s/,$//' > list.txt

#This will generate a oneliner in the following format to be applied later using the UPDATE option in the aws-organizations-alternate-contact-manager.
' 000000000001,000000000002,000000000003,000000000004'
# This will be used to alter or modify the contacts.
