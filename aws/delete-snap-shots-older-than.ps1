#trocar o owner id baseado na conta que voce quer limpar
#verifique se  vc tem permissao pra usar o diretorio onde ele salva o .json

#powershell

aws ec2 describe-snapshots --query 'Snapshots[?StartTime<=`2021-01-01`].SnapshotId' --owner-ids '#your_account_id' --output json --profile prdsvc --region us-west-2 > C:\script\snaps.json

$jsonobject = Get-Content C:\script\snaps.json | ConvertFrom-Json

# actual deletion
ForEach ($snap in $jsonobject)
{
    aws ec2 delete-snapshot --snapshot-id $snap --dry-run --output text --profile prdsvc --region us-west-2
}
