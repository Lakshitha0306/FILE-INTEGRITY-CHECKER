# 🛡 File Integrity Checker 

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : LAKSHITHA R

*INTERN ID* : CITSOD467

*DOMAIN* : CYBER SECURITY AND ETHICAL HACKING 

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

---

# 🛡 File Integrity Checker – Task 1

📌 Description

This is a Python-based File Integrity Checker built as part of Task 1 for the CodTech IT Internship in the Cyber Security domain.

The tool monitors and ensures the integrity of files in a specified folder by calculating and storing their SHA-256 hash values. On each run, it compares the current hash of each file with previously stored hashes to detect any modification, tampering, or addition of files.

It is a lightweight and effective utility for identifying unauthorized changes to important files — a fundamental step in maintaining system security.


---

✅ Features

Calculates secure SHA-256 hash for each file

Detects new, modified, or tampered files

Stores hash values in a local JSON file for future comparisons

Simple to use and easy to customize



---

🚀 How to Use

1. 📁 Set Up the Folder to Monitor

Create or choose a folder with files you want to monitor.
Update the FOLDER_PATH in the script with the full path of that folder.

Example:
FOLDER_PATH = "C:/Users/Lakshitha/Desktop/task1_files"

2. 🧪 Run the Script

Open a terminal or command prompt and run:

python file_integrity_checker.py

On the first run: Hashes of files are stored in file_hashes.json.

On the next run: It compares and tells you if files were changed or added.



---

🧩 Requirements

Python 3.x

Uses only standard Python libraries:

os

hashlib

json



No external libraries required!


---

📁 Files in This Project

file_integrity_checker.py – Main Python script

README.md – Project overview and usage guide



---

🔒 Note

The script creates a file called file_hashes.json to store hash values.
You can delete it if you want to reset and start fresh.

*OUTPUT:

![Image](https://github.com/user-attachments/assets/391cdd93-4478-422a-80ab-ff72dcb3d705)
