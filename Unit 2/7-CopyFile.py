# 7. Write a program to copy a text file using file handling mechanism. 

try:
    source_file = "src.txt"
    destination_file = "destination.txt"

    with open(source_file, "r", encoding="utf-8") as src:
        content = src.read()

    with open(destination_file, "w", encoding="utf-8") as dest:
        dest.write(content)

    print("File copied successfully!")
except FileNotFoundError:
    print("Error: src.txt file not found!")
except Exception as e:
    print("Error:", e)
