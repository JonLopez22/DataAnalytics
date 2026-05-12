# with parameters and arugmenmts

def greeting(name, city, hobby) :
    return name, city, hobby

result = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

print (type(result))

print(f"Hello, {result[0]}! You are from {result[1]} and your hobby is {result[2]}.")

# unpack as variables

def greeting(name, city, hobby) :
    return name, city, hobby

name, city, hobby = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

print(f"Hello, {name}! You are from {city} and your hobby is {hobby}.")