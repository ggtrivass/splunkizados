# Detecting Encoded PowerShell Commands

## Objective

Detect suspicious PowerShell encoded execution.

---

## SPL Query

```spl
index=wineventlog EventCode=4688 powershell.exe
| search CommandLine="*EncodedCommand*"
```

---

## Why It Is Suspicious

Attackers often use encoded commands to:

- Obfuscate payloads
- Evade detection
- Execute malicious scripts

---

## MITRE ATT&CK

- T1059.001 — PowerShell
