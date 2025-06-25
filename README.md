# 🛡 File Integrity Checker 

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : LAKSHITHA R

*INTERN ID* : CITSOD467

*DOMAIN* : CYBER SECURITY AND ETHICAL HACKING 

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH
---

# 🛡 File Integrity Checker – Task 1

## 📌 Description
This is a Python-based File Integrity Checker built as part of *Task 1 for the CodTech IT Internship* in the *Cyber Security domain*.

The tool monitors and ensures the integrity of files in a specified folder by calculating and storing their *SHA-256 hash values. On each run, it compares the current hash of each file with previously stored hashes to detect any **modification, tampering, or addition* of files.

It is a lightweight and effective utility for identifying unauthorized changes to important files — a fundamental step in maintaining system security.

---

## ✅ Features
- Calculates secure *SHA-256 hash* for each file
- Detects *new, modified, or tampered files*
- Stores hash values in a local JSON file for future comparisons
- Simple to use and easy to customize

---

## 🚀 How to Use

### 1. 📁 Set Up the Folder to Monitor
Create or choose a folder with files you want to monitor. Update the script’s FOLDER_PATH variable with that folder's full path.

Example:
```python
FOLDER_PATH = "C:/Users/Lakshitha/Desktop/task1_files"


---

2. 🧪 Run the Script

Use a terminal or command prompt to run the script:

python file_integrity_checker.py

On first run: It stores hash values of all files into file_hashes.json.

On next runs: It compares hashes and reports any file that changed or was added.



---

🧩 Requirements

Python 3.x

Standard Python libraries:

os

hashlib

json



> No external libraries required. Works out of the box!




---

📁 Files in This Project

File	Purpose

file_integrity_checker.py	Main Python script
README.md	Project overview and usage guide



---

🔒 Note

The script generates a file named file_hashes.json to store the hash values. You can delete it if you want to reset the baseline
