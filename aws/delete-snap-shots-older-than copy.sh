#trocar o owner id baseado na conta que voce quer limpar
#verifique se  vc tem permissao pra usar o diretorio onde ele salva o .json
####BASH

snapshots_to_delete=$(aws ec2 describe-snapshots --owner-ids '#your_account_id' --query 'Snapshots[?StartTime<=`2021-01-01`].SnapshotId' --output text)
echo "List of snapshots to delete: $snapshots_to_delete"

# actual deletion
for snap in $snapshots_to_delete; do
  aws ec2 delete-snapshot --snapshot-id $snap --dry-run
  echo $snap deletado
done
