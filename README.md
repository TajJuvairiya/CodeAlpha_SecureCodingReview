# CodeAlpha_SecureCodingReview
# Secure Coding Review — Python Vulnerability Assessment 🔍

A static code review conducted on a vulnerable Python application as part of the **CodeAlpha Cybersecurity Internship** (Task 3).

## 📋 About
This project involves a manual security audit of a Python authentication application. The review identifies 10 security vulnerabilities, explains how each can be exploited, and provides remediated code with best practice recommendations.

## 📁 Files

| File | Description |
|------|-------------|
| `vulnerable_app.py` | The Python application that was reviewed |
| `SecureCodeReview_Report.docx` | Full findings report with vulnerabilities and fixes |

## 🔓 Vulnerabilities Found

| ID   | Vulnerability                          | Severity     |
|----  |----------------------------------------|--------------|
| V-01 | SQL Injection                          | 🔴 CRITICAL |
| V-02 | Command Injection                      | 🔴 CRITICAL |
| V-03 | Insecure Deserialization (Pickle)      | 🔴 CRITICAL |
| V-04 | Hardcoded Credentials & Secret Keys    | 🟠 HIGH     |
| V-05 | Path Traversal                         | 🟠 HIGH     |
| V-06 | Weak Password Hashing (MD5)            | 🟠 HIGH     |
| V-07 | Plaintext Password Storage             | 🟠 HIGH     |
| V-08 | Sensitive Data Exposure                | 🟡 MEDIUM   |
| V-09 | Bare Except / Broad Exception Handling | 🟡 MEDIUM   |
| V-10 | Debug Mode Enabled in Production       | 🟢 LOW      |

## 🛠️ Methodology
- Manual line-by-line static code inspection
- Identification of dangerous function calls (pickle, subprocess, hashlib.md5)
- Tracing user-controlled data flows from input to output
- Standards referenced: OWASP Top 10, CWE/SANS Top 25

## 🏢 Internship
**Organization:** CodeAlpha  
**Domain:** Cyber Security  
**Task:** Task 3 — Secure Coding Review
By Taj Juvairiya Khan
