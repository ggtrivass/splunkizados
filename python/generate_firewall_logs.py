from datetime import datetime
import random
import time

src_ips = [
    "10.0.0.8",
    "192.168.1.15",
    "201.10.50.23",
    "172.16.1.5"
]

dest_ips = [
    "192.168.1.5",
    "192.168.1.10",
    "10.10.10.5"
]

ports = [22, 80, 443, 3389, 8080, 445]

protocols = ["TCP", "UDP"]

actions = ["ALLOW", "DENY"]

log_file = r"C:\splunk-lab\logs\firewall.log"

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    src_ip = random.choice(src_ips)
    dest_ip = random.choice(dest_ips)
    port = random.choice(ports)
    protocol = random.choice(protocols)
    action = random.choice(actions)

    log_line = (
        f"{timestamp} FIREWALL {action} "
        f"src={src_ip} dest={dest_ip} "
        f"port={port} protocol={protocol}\n"
    )

    with open(log_file, "a") as f:
        f.write(log_line)

    print(log_line.strip())

    time.sleep(2)
