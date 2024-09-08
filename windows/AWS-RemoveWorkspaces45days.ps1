$region = "us-east-1"

Initialize-AWSDefaultConfiguration -Region $region
$ID = Get-WKSWorkspacesConnectionStatus | ? {$_.LastKnownUserConnectionTimestamp -lt (Get-Date).AddDays(-45)}
$list = $ID | foreach-object {Get-WKSWorkspace -WorkspaceId $_.WorkspaceId}
$list.count
$list | ft -autosize

#Delete workspaces 
$listWorkspaceId = $lista | Select WorkspaceId
$listWorkspaceId | foreach-object {Remove-WKSWorkspace -WorkspaceId $_.WorkspaceId -Confirm:$False}