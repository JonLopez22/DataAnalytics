# Define a function with no parameters

def greeting() :
    name = input("Please enter your name: ")
    return name

result = greeting
print(f"Hello, {result()}!")
