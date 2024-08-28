#!/bin/bash
# get json from all dbs and make a table format of it, no need to use loop as jq do the heavy lifting for us

# Output example:
# Database Name: supermegaultradatabase
# Instance Size: db.t3.medium
# Multi-AZ: true/false
# Disk Type: gp2 / gp3 / standard
# Encrypted: true/false ( just returns the value of the field)
# Size (GB): 20 (min 20gbs)
# Max Storage (GB): 40 or N/A

# known issues
# Clustered DBs
#  - 1 replicas always use standard disks and sizing is 1
#  - max storage and multi-az bugs as well

echo '### Listing all databses and its statuses ###'
aws rds describe-db-instances --query 'DBInstances[*]' --output json | jq -r '.[] | "Database Name: \(.DBInstanceIdentifier)\nInstance Size: \(.DBInstanceClass)\nMulti-AZ: \(.MultiAZ)\nDisk Type: \(.StorageType)\nEncrypted: \(.StorageEncrypted)\nSize (GB): \(.AllocatedStorage)\nMax Storage (GB): \(.MaxAllocatedStorage // "N/A")\n---"'
echo "### done ###"
