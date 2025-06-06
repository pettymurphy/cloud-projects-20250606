#!/bin/bash

# Title: check_cves.sh
# Description: Scans Ubuntu system for available security updates with CVE references

echo "----------------------------"
echo " CVE SECURITY SCAN (Ubuntu)"
echo "----------------------------"

# Check if 'unattended-upgrades' is installed
if ! command -v unattended-upgrade &> /dev/null; then
    echo "Installing unattended-upgrades..."
    sudo apt install unattended-upgrades -y
fi

echo ""
echo "Fetching security updates..."
sudo unattended-upgrade --dry-run -d | grep -i cve

echo ""
echo "Done. Review the above CVEs and patch accordingly."

#What this does:
#Checks if unattended-upgrade is installed.

#Runs a dry-run to simulate which packages would be updated for security.

#Greps out any lines mentioning CVEs.