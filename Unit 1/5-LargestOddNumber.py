#Write a program to enter 10 numbers and display largest odd number from the entered number

odd = []

print("Enter 10 numbers:")
for i in range(10):
    n = int(input())
    if n % 2 == 1:
        odd.append(n)


if odd:
    print("Largest odd number is ",max(odd))

else:
    print("No odd numbers found")




