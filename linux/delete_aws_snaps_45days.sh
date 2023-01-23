#!/bin/bash
# Current date, today
current_date=$(date +%s)

# Convert 45 days to seconds
expiration_date=$((45 * 24 * 60 * 60))

# Iterate through all snapshots
for snapshot_id in $(aws ec2 describe-snapshots --query 'Snapshots[*].SnapshotId' --output text); do
    # Get the snapshot creation date
    creation_date=$(aws ec2 describe-snapshots --snapshot-ids $snapshot_id --query 'Snapshots[*].StartTime' --output text)
    # Convert the snapshot creation date to a timestamp
    creation_timestamp=$(date -d "$creation_date" +%s)
    # Calculate the difference between the current date and the snapshot creation date
    age=$((current_date - creation_timestamp))
    # If the snapshot is older than 45 days
    if [[ $age -gt $expiration_date ]]; then
        # Delete the snapshot
        aws ec2 delete-snapshot --snapshot-id $snapshot_id
    fi
done

#improvements to be made
