import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =========================
FIREWALL_IP = "150.242.201.80"
API_TOKEN = "3gd5QyQ1bpwtpgy1csG4hqH8nznQ5x"
# =========================

url = f"https://{FIREWALL_IP}:9443/api/v2/monitor/vpn/ipsec"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

response = requests.get(url, headers=headers, verify=False)

print("HTTP Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    tunnels = data.get("results", [])

    print("\n🔐 IPsec VPN Tunnel Status:\n")

    for tunnel in tunnels:
        name = tunnel.get("name")
        tunnel_status = tunnel.get("tunnel")

        # Agar status 1/0 format me ho
        if tunnel_status == 1:
            readable_status = "UP"
        elif tunnel_status == 0:
            readable_status = "DOWN"
        else:
            readable_status = tunnel_status

        print(f"Tunnel Name: {name}")
        print(f"Status: {readable_status}")
        print("-" * 40)

    with open("vpn_status.json", "w") as f:
        json.dump(data, f, indent=4)

    print("\n📁 Full VPN data saved to vpn_status.json")

else:
    print("❌ Failed to fetch VPN status")