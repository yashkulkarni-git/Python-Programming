'''8. Write a Python program to perform following operation on given string input:
a) Count Number of Vowel in given string
b) Count Length of string (donot use len() )
c) Reverse string
d) Find and replace operation
e) check whether string entered is a palindrome or not'''

def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            count += 1
    return count

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

def find_and_replace(s):
    find = input("Enter substring to find: ")
    replace = input("Enter substring to replace with: ")
    return s.replace(find, replace)

def check_palindrome(s):
    rev = reverse_string(s)
    if s == rev:
        return True
    else:
        return False

string = input("Enter a string: ")

while True:
    print("\n--- MENU ---")
    print("1. Count number of vowels")
    print("2. Count length of string")
    print("3. Reverse string")
    print("4. Find and replace")
    print("5. Check palindrome")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Number of vowels:", count_vowels(string))

    elif choice == 2:
        print("Length of string:", string_length(string))

    elif choice == 3:
        print("Reversed string:", reverse_string(string))

    elif choice == 4:
        string = find_and_replace(string)
        print("Updated string:", string)

    elif choice == 5:
        if check_palindrome(string):
            print("The string is a palindrome")
        else:
            print("The string is not a palindrome")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
