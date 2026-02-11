# 13.Write a program to make use of map(), filter() and reduce() functions with context to lambda functions. 


from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. Map: Square each number
squared = list(map(lambda x: x**2, numbers))

# 2. Filter: Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# 3. Reduce: Multiply all numbers together (1*2*3*4*5*6)
product = reduce(lambda x, y: x * y, numbers)

print(f"Original: {numbers}")
print(f"Squared (Map): {squared}")
print(f"Evens (Filter): {evens}")
print(f"Product (Reduce): {product}")