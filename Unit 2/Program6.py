#Write a program to read a file which contains only numbers. Display total
#of all numbers with maximum and minimum number
total = 0
filepath="numbers.txt"

with open(filepath,"r") as file:
    for line in file:
        num=int(line.strip())
        total+=num


maximum=0
minimum=0
if maximum is None or num > maximum:
    maximum = num

if minimum is None or num < minimum:
    minimum = num
    
print("Total of all numbers is ",total)
print("Maximum number is ",maximum)
print("Minimum number is ",minimum)



