# Python Scripts

This folder contains Python scripts used to simulate security-related activity for Splunk ingestion and detection engineering practice.

---

# generate_logs.py

Simulates:

- Failed login attempts
- PowerShell encoded command execution
- Mimikatz activity
- External RDP access
- Successful authentication events

## Usage

```bash
python generate_logs.py
```

## Output Example

```text
2026-05-14 14:48:34 ALERT powershell.exe -enc suspicious payload from 201.10.50.23
2026-05-14 14:48:40 ALERT mimikatz.exe executed from 172.16.1.5
```
---

# generate_firewall_logs.py

Simulates:

- Firewall ALLOW/DENY events
- External connections
- RDP traffic (3389)
- Multiple protocols (TCP/UDP)
- Source and destination IP activity

## Usage

```bash
python generate_firewall_logs.py
```

## Output Example

```text
2026-05-14 15:05:05 FIREWALL ALLOW src=201.10.50.23 dest=192.168.1.10 port=8080 protocol=UDP
2026-05-14 15:05:07 FIREWALL DENY src=172.16.1.5 dest=10.10.10.5 port=3389 protocol=TCP
```
