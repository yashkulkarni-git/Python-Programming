# 12.Write a program to display the use of local, global and nonlocal variables 

x = "Global" 

def outer_function():
    x = "Enclosing (Local to Outer)"
    
    def inner_function():
        nonlocal x
        x = "Modified Nonlocal"
        print("Inner:", x)

    def local_demo():
        x = "Strictly Local"
        print("Local Demo:", x)

    local_demo()
    inner_function()
    print("Outer after inner call:", x)

print("Before function:", x)
outer_function()
print("Global after function:", x)