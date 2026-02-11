# 10.Write a program to create 4 lambda functions which shall accept 2 numbers and one arithmetic operator. As per arithmetic operator related lambda functions shall be invoked.

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y if y != 0 else "Error: Division by zero"

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    try:
        num1 = float(input("Enter First number: "))
        num2 = float(input("Enter Second number: "))
        op = input("Enter operator (+, -, *, /): ")

        if op in operations:
            result = operations[op](num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid operator!")
            
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    calculator()
