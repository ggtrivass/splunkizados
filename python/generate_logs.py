from datetime import datetime
import random
import time

ips = [
    "10.0.0.8",
    "192.168.1.15",
    "201.10.50.23",
    "172.16.1.5"
]

events = [
    "INFO User triv logged in successfully",
    "WARN Failed login attempt for user admin",
    "ALERT mimikatz.exe executed",
    "ALERT powershell.exe -enc suspicious payload",
    "WARN RDP login from external IP"
]

log_file = r"C:\splunk-lab\logs\live.log"

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ip = random.choice(ips)
    event = random.choice(events)

    log_line = f"{timestamp} {event} from {ip}\n"

    with open(log_file, "a") as f:
        f.write(log_line)

    print(log_line.strip())

    time.sleep(2)
