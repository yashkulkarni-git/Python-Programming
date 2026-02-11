# 11.Write a program to create function which shall accept any number of arguments and display total of all the numbers given as argument. 

def calculate_total(*args):
    total = sum(args)
    print(f"Numbers: {args}")
    print(f"Total Sum: {total}")

user_input = input("Enter numbers: ")

try:
    numeric_list = [float(num) for num in user_input.split()]
    calculate_total(*numeric_list)
except ValueError:
    print("Invalid input.")