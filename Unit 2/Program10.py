# 10. Write a program to zip and unzip particular files.

import zipfile
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def zip_files():
    files_input = input("Enter file names to zip (comma separated): ")
    files = [f.strip() for f in files_input.split(",")]
    zip_name = input("Enter zip file name (e.g., myfiles.zip): ").strip()

    zip_path = os.path.join(BASE_DIR, zip_name)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            file_path = os.path.join(BASE_DIR, file)
            if os.path.exists(file_path):
                zipf.write(file_path, arcname=file)
                print(f"Added: {file}")
            else:
                print(f"Skipped (not found): {file}")

    print(f"Zipping completed! Saved at: {zip_path}\n")


def unzip_files():
    zip_name = input("Enter zip file name to unzip: ").strip()
    extract_to = input("Enter folder name to extract to: ").strip()

    zip_path = os.path.join(BASE_DIR, zip_name)
    extract_path = os.path.join(BASE_DIR, extract_to)

    if not os.path.exists(zip_path):
        print("Zip file not found in the script folder!\n")
        return

    with zipfile.ZipFile(zip_path, "r") as zipf:
        zipf.extractall(extract_path)

    print(f"Unzipping completed! Extracted to: {extract_path}\n")


while True:
    print("====== ZIP / UNZIP Menu ======")
    print("a) Zip particular files")
    print("b) Unzip files")
    print("c) Exit")

    choice = input("Enter your choice: ").lower().strip()

    if choice == "a":
        zip_files()
    elif choice == "b":
        unzip_files()
    elif choice == "c":
        print("Exiting program. Bye 👋")
        break
    else:
        print("Invalid choice! Try again.\n")
