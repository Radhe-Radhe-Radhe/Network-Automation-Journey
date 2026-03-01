import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =====================
# 🔹 EDIT THIS
# =====================
FIREWALL_IP = "150.242.201.80"
API_TOKEN = "3gd5QyQ1bpwtpgy1csG4hqH8nznQ5x"
# =====================

url = f"https://{FIREWALL_IP}:9443/api/v2/cmdb/firewall/policy"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

response = requests.get(url, headers=headers, verify=False)

print("HTTP Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    policies = data.get("results", [])

    print("Total Firewall Policies:", len(policies))
else:
    print("❌ Failed to fetch firewall policies")