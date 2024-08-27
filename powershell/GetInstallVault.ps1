#You MUST define your directory otherwise it will not work
# Retrieve .cer and .key files from a vault kv, bundle them together in a pfx file, install it and cleanup afterwards.
# Useful for Windows IIS environments.
# tested to exhaustion, any issues please contact me :)
# If this was useful consider buyin me a coffe https://buymeacoffee.com/tbrondani

#Variables

$workingDir = "Your_Dir"
mkdir $workingDir -ErrorAction SilentlyContinue

$body = @{
    'role_id'='your_vault_role_id'
    'secret_id'='your_secret_id'
}

$logurl="https://your_vault_login_url"
$tokurl="https://your_vault_secret_url"


function GenerateVaultToken
{


#login method
$Response= Invoke-WebRequest -Method 'Post' -Uri $logurl -Body $body

#convert to json
$json = $Response.Content | ConvertFrom-Json

#filter json
$tokenfile=$json.auth.client_token | Out-File $workingDir\token.txt

#$token=$json.auth.client_token

}

function GenerateVaultCertificates{

$token= Get-Content $workingDir\token.txt
$headers = @{
    'X-Vault-Token'=$token
}

$GetToken= Invoke-WebRequest -Method 'Get' -Uri $tokurl -Header $headers
$GetToken.Content

$cer= $GetToken.Content | ConvertFrom-Json

#create files 
$privatek=$cer.data.data.'private-cert' | Out-File $workingDir\vault-cert.key
$public=$cer.data.data.'public-chain-cer' | Out-File $workingDir\vault-cert.cer

}

function ImportLocalVaultCertificates{
##first password parameter must be dummy and second should be the actual password due powershell bug
certutil -p "1,000000" -f -v –MergePFX $workingDir\vault-cert.cer $workingDir\vault-cert.pfx

$SecString_bneon = '000000'

Import-PfxCertificate -FilePath $workingDir\vault-cert.pfx -Password (ConvertTo-SecureString -String $SecString_bneon -AsPlainText -Force) -CertStoreLocation cert:\LocalMachine\My
}

function CertsCleanup{
 #cleanup
 Remove-Item $workingDir\*.*
}

CertsCleanup
GenerateVaultToken
GenerateVaultCertificates
ImportLocalVaultCertificates

#CertsCleanup
