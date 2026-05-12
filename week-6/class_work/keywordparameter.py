# default parameters are also called keyword parameters
# make the arugment optional at call time

def greeting(name = "Unknown", hobby = "Nothing",city = "New York") :
    return f"Hello, {name}! You are from {city} and you enjoy {hobby}."

# Call 1, no arguements, use default values
result1 = greeting()
print(result1)

# call 2, name only provided, use default values for hobby and city
result2 = greeting(name = "Alice")
print(result2)

# Call 3, all three arguements provided, all defaults overridden
result3 = greeting(name = "Bob", hobby = "painting", city = "Los Angeles")
print(result3)

# Call 4, using input() to let the user supply all three values
result4 = greeting(
    name = input("Please enter your name: "),
    hobby = input("Please enter your hobby: "),
    city = input("Please enter your city: ")
)

print(result4)