#!/bin/bash

# Title: check_rhel_cves.sh
# Description: Checks RHEL/CentOS system for available security updates and CVEs
#Make sure the yum-plugin-security package is installed:
#sudo yum install yum-plugin-security -y


echo "----------------------------"
echo " CVE SECURITY SCAN (RHEL)"
echo "----------------------------"

# Make sure yum security plugin is available
if ! yum --security check-update &> /dev/null; then
    echo "Security plugin not available or not supported on this system."
    exit 1
fi

echo ""
echo "Available security updates with CVE info:"
yum updateinfo list security all

echo ""
echo "To see advisories by severity:"
yum updateinfo list security all | grep -E "Important|Critical"

echo ""
echo "Done. Patch as needed based on severity."

#yum updateinfo provides details on security advisories and may include CVEs if available in your repo metadata.