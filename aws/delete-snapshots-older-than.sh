#list all snaps
snapshots_to_delete=$(aws ec2 describe-snapshots --owner-ids xxxxxxxxxxx --query 'Snapshots[?StartTime<=`2021-01-01`].SnapshotId' --output text)
echo "List of snapshots to delete: $snapshots_to_delete"

# actual deletion use with caution
for snap in $snapshots_to_delete; do
  aws ec2 delete-snapshot --snapshot-id $snap --dry-run
  echo $snap deletado
done
