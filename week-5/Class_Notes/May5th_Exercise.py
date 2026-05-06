name1 = "Chantal Lee"
name2 = "Dimitri Nji"
name3 = "Vesna Cari"
print(f"Hello, {name1}! "f"Hello, {name2}! "f"Hello, {name3}! ")
# Could have used print(f"Hello, {name1}! /n Hello, {name2}! /n Hello, {name3}! ")
print(f"Hello, {name1}!\nHello, {name2}!\nHello, {name3}!")

# importing math module
import math
print(f"value of pi: {math.pi:.2f}")

from math import pi
print(f"value of pi: {pi:.2f}")

num1 = 10
print(type(num1))
print(type(str(num1)))

num2 = '25'
print(type(num2))
print(type(int(num2)))

print(type(float(num2)))
print(float(num2))

num3 = 3.14569
print(round(num3, 2))

# Accept multiple inputs on one line


def rectangle_area(length, width):
    area = length * width
    return area


if __name__ == "__main__":
    length,width = input("Enter the length and width of the rectangle: ").split()
    length = float(length)
    width = float(width)

    result = rectangle_area(length, width)

print(f"The area of the rectangle is {result:.2f}")
print(f"The perimeter of the rectangle is {perimeter:.2f}")