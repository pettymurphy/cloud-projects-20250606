# PACKAGE SCANNER SCRIPT

# 1. Ask the user to enter package names, separated by commas
user_input = input("Enter package names (comma-separated): ")

# 2. Split the input into a list
packages = user_input.split(",")

# 3. Loop through each package in the list
for pkg in packages:
    pkg = pkg.strip()  # Remove extra spaces
    # 4. Simulate checking if it's installed (just for demo)
    if pkg.lower() in ["curl", "git", "python3"]:
        print(f"✅ Package '{pkg}' is installed.")
    else:
        print(f"❌ Package '{pkg}' is NOT installed.")

