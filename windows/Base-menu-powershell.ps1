$aws_region = potato

function Show-Menu
{
     param (
           [string]$Title = 'Projeto_xyz'
     )
     cls
     Write-Host "================ $Title - aperte "q" para sair ================"
     Write-Host "================ $aws_region ================"
     Write-Host "1: Task 1."
     Write-Host "2: Task 2."
     Write-Host "3: Task 3."
     Write-Host "4: Task 4."
     Write-Host "5: Task 5."
     Write-Host "6: Task 6."
     Write-Host "7: Task 7."
    }

do
{
     Show-Menu
     $input = Read-Host "Please make a selection"
     switch ($input)
    {       
             '1'{
                fgroup_create_list
           } '2'{
                fgroup_status_list
           } '3' {
                fgroup_modify_enable
           } '4' {
                fgroup_modify_disable
           } '5' {
                fsingle_status
           } '6' {
                fsingle_modify_enable
           } '7' {
                fsingle_modify_disable
           } 'q' {
                return
           }
     }
     pause
}
until ($input -eq 'q')