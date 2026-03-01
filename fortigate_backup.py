import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =====================
# EDIT THESE
# =====================
FIREWALL_IP = "150.242.201.80"

API_TOKEN = "3gd5QyQ1bpwtpgy1csG4hqH8nznQ5x"
# =====================

url = f"https://{FIREWALL_IP}:9443/api/v2/monitor/system/config/backup?scope=global"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

response = requests.get(url, headers=headers, verify=False)

print("Status Code:", response.status_code)

if response.status_code == 200:
    with open("fortigate_backup.conf", "wb") as f:
        f.write(response.content)
    print("✅ Backup downloaded successfully")
else:
    print("❌ Backup failed")
    print("Response:", response.text)
    
    from send_email import send_email

FIREWALL_NAME = "Audix-FG-60F"

status_message = "Backup completed successfully. Firewall is operational."

send_email(
    firewall_name=FIREWALL_NAME,
    status_message=status_message,
    attachment_path="backup.conf"
)