import subprocess

# Ask the user to enter a package name
package = input("Enter the name of the package to check: ")

# Run a shell command to check installed packages
result = subprocess.run(["dpkg", "-l", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Conditional logic to check output
if "no packages found" in result.stderr.lower() or result.returncode != 0:
    print(f"❌ Package '{package}' is NOT installed.")
else:
    print(f"✅ Package '{package}' IS installed.")
