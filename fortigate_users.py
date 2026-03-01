import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

FIREWALL_IP = "150.242.201.80"
API_TOKEN = "3gd5QyQ1bpwtpgy1csG4hqH8nznQ5x"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Get Users
users_url = f"https://{FIREWALL_IP}:9443/api/v2/cmdb/user/local"
groups_url = f"https://{FIREWALL_IP}:9443/api/v2/cmdb/user/group"

# ---- Users ----
response_users = requests.get(users_url, headers=headers, verify=False)

print("\n👤 Local Users:\n")

if response_users.status_code == 200:
    users = response_users.json().get("results", [])
    for user in users:
        print("Username:", user.get("name"))
        print("Status:", user.get("status"))
        print("-" * 30)
else:
    print("Failed to fetch users")

# ---- Groups ----
response_groups = requests.get(groups_url, headers=headers, verify=False)

print("\n👥 User Groups:\n")

if response_groups.status_code == 200:
    groups = response_groups.json().get("results", [])
    for group in groups:
        print("Group Name:", group.get("name"))
        print("Members:", group.get("member"))
        print("-" * 30)
else:
    print("Failed to fetch groups")