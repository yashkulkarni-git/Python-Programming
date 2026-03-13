#Write a program to enter 10 numbers and display all armstrong numbers from those numbers.

numbers = []

print("Enter 10 numbers:")
for i in range(10):
    n = int(input())
    numbers.append(n)

print("armstrong numbers are")
for num in numbers:
    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d) ** power

    if total == num:
        print(num)
