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

# 10-minute quick check

# name = input("Enter your name: ")
# num1 = float(input("Enter your first number: "))
# num2 = float(input("Enter your second number: "))
# num3 = float(input("Enter your third number: "))

#average = (num1 + num2 + num3) / 3

# print(f"Hello, {name}! The average of the three numbers you entered is: {average:.2f}")

# original_price = float(input("Enter the original price: "))
# discount_percentage = float(input("Enter the discount percentage: "))
# discount_amount = original_price * (discount_percentage / 100)
# final_price = original_price - discount_amount
# print(f"Final Price = ${final_price:.2f}")

# Cost of meal
meal_cost = float(input("Enter the cost of the meal: $"))

tip = meal_cost * 0.20
tax = meal_cost * 0.0825
total_cost = meal_cost + tip + tax

print("\n----- Meal Cost Breakdown -----")
print(f"{'Meal Cost:':<15} ${meal_cost:>6.2f}")
print(f"{'Tip (20%):':<15} ${tip:>6.2f}")
print(f"{'Tax (8.25%):':<15} ${tax:>6.2f}")
print("------------------------------")
print(f"{'Total Cost:':<15} ${total_cost:>6.2f}")