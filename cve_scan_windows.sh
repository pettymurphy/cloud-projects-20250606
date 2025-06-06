# Title: Check-WindowsUpdates.ps1
# Description: List missing security patches and CVE IDs (if available)
#🔹 You may need to install PSWindowsUpdate:
#Install-Module PSWindowsUpdate -Force


Write-Output "-----------------------------"
Write-Output " CVE Security Scan (Windows)"
Write-Output "-----------------------------"

# Import Update module
Import-Module PSWindowsUpdate

# List available updates
Get-WindowsUpdate -MicrosoftUpdate -AcceptAll -IgnoreReboot | 
    Select-Object Title, KB, Severity | 
    Format-Table -AutoSize
