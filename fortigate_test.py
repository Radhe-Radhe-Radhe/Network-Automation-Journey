import requests
import json

# Disable SSL warnings (only for lab/testing)
requests.packages.urllib3.disable_warnings()

# ==============================
# FORTIGATE DETAILS
# ==============================
firewall_ip = "https://150.242.201.80:9443"
api_token = "3gd5QyQ1bpwtpgy1csG4hqH8nznQ5x"

headers = {
    "Authorization": f"Bearer {api_token}"
}

# Safe Read-Only Endpoint
url = f"{firewall_ip}/api/v2/monitor/system/status"

try:
    response = requests.get(url, headers=headers, verify=False, timeout=5)

    print("HTTP Status Code:", response.status_code)

    if response.status_code == 200:
        print("✅ Firewall Connected Successfully\n")

        data = response.json()

        # Print important safe fields only
        print("Hostname:", data.get("hostname"))
        print("Version:", data.get("version"))
        print("Serial Number:", data.get("serial"))
        print("Uptime:", data.get("uptime"))

        # Save full response to file
        with open("fortigate_status.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\n📁 Full status saved to fortigate_status.json")

    elif response.status_code == 401:
        print("❌ Unauthorized - Check API Token")

    else:
        print("⚠ Connected but unexpected response:", response.status_code)

except Exception as e:
    print("❌ Connection Failed")
    print("Error:", e)
