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
