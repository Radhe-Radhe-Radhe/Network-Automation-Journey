import os

print("Checking connectivity to 8.8.8.8 ...")

response = os.system("ping 8.8.8.8")

if response == 0:
    print("Network is UP")
else:
    print("Network is DOWN")
    