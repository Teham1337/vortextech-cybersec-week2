# Password Strength Evaluator
---
A simple Python script that evaluates password strength based on length, character variety, and common password checks.

## Features
Checks for minimum length of 8 characters.

Checks for uppercase, lowercase, numbers, and special characters.

Flags common passwords like 123456 or password as Very Weak.

Displays a rating (Weak, Medium, Strong) along with feedback.

## Logic
The script evaluates passwords using three main steps:
1. **Blacklist Check:** Compares the input against a list of common passwords (e.g., `123456`, `password`). If matched, it immediately flags it as **Very Weak**.
2. **Criteria Validation:** Checks for minimum length (8+ characters) and character variety (uppercase, lowercase, digits, special characters) using Python's `any()` function.
3. **Rating & Feedback:** Calculates a score based on passed criteria to assign a rating (**Weak**, **Medium**, or **Strong**) and appends specific feedback for any missing requirements.

## How To Run It
---
Open your terminal or command prompt in the project directory and then run the script using Python 3.

## Example Output
---
Password: '123456'
Strength: Very Weak
Feedback: This is an extremely common password. Choose something unique.

Password: 'TehamIrfan21!'
Strength: Strong
Feedback: Perfect password structure!

## Reflection On Real-World Risks
---
Weak or predictable passwords allow attackers to gain unauthorized access via brute-force attacks or credential stuffing, easily bypassing authentication systems.

---

# Nmap Scan Results Analysis
---
Target: localhost (127.0.0.1)
Command: nmap localhost
Open Ports Found:
---
## Port 135/tcp (Service: msrpc)
Description: Microsoft Remote Procedure Call (RPC).
Meaning: Used by Windows operating systems to coordinate communication between client and server applications.

## Port 445/tcp (Service: microsoft-ds)
Description: Microsoft Directory Services (SMB - Server Message Block).
Meaning: Used for network file sharing, printer sharing, and remote administrative functions across local networks.

## Reflection On Real-World Analysis
---
Exposed Local Services: Ports 135 and 445 are common targets on Windows environments. Unpatched or improperly secured SMB services (Port 445) are historically vulnerable to ransomware (like WannaCry) and lateral movement attacks across internal networks.
