import os
import hashlib
import json

FOLDER_PATH = "C:/Users/YourName/Desktop/task1"
HASH_STORE_FILE = "file_hashes.json"

def calculate_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def load_hashes():
    if os.path.exists(HASH_STORE_FILE):
        with open(HASH_STORE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_STORE_FILE, 'w') as f:
        json.dump(hashes, f, indent=4)

def scan_and_check():
    current_hashes = {}
    old_hashes = load_hashes()
    changed_files = []

    for root, _, files in os.walk(FOLDER_PATH):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = calculate_hash(filepath)
            current_hashes[filepath] = file_hash

            if filepath in old_hashes:
                if old_hashes[filepath] != file_hash:
                    changed_files.append(filepath)
            else:
                changed_files.append(filepath)

    save_hashes(current_hashes)

    if changed_files:
        print("⚠ Changed or new files detected:")
        for f in changed_files:
            print(f"- {f}")
    else:
        print("✅ No changes detected.")

if __name__ == "__main__":
    print("🔍 Scanning for file changes...")
    scan_and_check()