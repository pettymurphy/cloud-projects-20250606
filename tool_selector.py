# List of DevOps tools
tools = ["awscli", "terraform", "ansible", "docker", "kubectl"]

# Print numbered tool list
print("Available Tools:")
for i in range(len(tools)):
    print(f"{i+1}. {tools[i]}")

# Ask user to select one
choice = int(input("Enter the number of the tool you want to use: "))

# Show the tool name they picked
if 1 <= choice <= len(tools):
    print(f"✅ You selected: {tools[choice - 1]}")
else:
    print("❌ Invalid choice. Please pick a number from the list.")
