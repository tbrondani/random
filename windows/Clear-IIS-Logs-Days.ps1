$path = "%SystemDrive%\inetpub\logs\LogFiles"
$days = "-7"

#---

$deletedate = (Get-Date).AddDays($days)
Get-ChildItem $path -include *.* -recurse | Where-Object {$_.LastWriteTime -lt $deletedate} | Remove-Item -Force -recurse -Confirm:$false