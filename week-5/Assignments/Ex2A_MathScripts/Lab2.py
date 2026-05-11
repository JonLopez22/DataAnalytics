# 1. Calculating Net Worth with assets and debts

# My assets
savings = 100000
car_value = 15000
investments = 50000
total_assets = savings + car_value + investments

# My Debts
car_loan = 5000
credit_card = 2000
total_debts = car_loan + credit_card

net_worth = total_assets - total_debts

print("Your total assets are: $" + str(total_assets))
print("Your total debts are: $" + str(total_debts))
print("Your net worth is: $" + str(net_worth))

# 2. Calculate area of a rectangle
side_a = 6
side_b = 29
area = side_a * side_b

print("Side A is " + str(side_a) + " and Side B is " + str(side_b))
print("The area of the rectangle is: " + str(area))

# 3. Calculate the tip amount on a restaurant bill given the tip percentage
bill = 45.00
tip_percent = 0.20
tip = bill * tip_percent

print("The tip on a $" + format(bill, ".2f") + " restaurant bill is $" + format(tip, ".2f"))

# 4. Calculate the area of a circle
import math
diameter = 29
radius = diameter / 2
area = math.pi * radius ** 2
print("The area of a circle with radius " + str(radius) + " is: " + format(area, ".2f"))

# 5. How long will it take a savings account worth X to double in value based on an interest rate of IR?
savings = 5000
interest_rate = 0.06
years = 72 / (interest_rate * 100)
doubled = savings * 2

print("Your current savings is $" + str(savings) + ".")
print("At a " + format(interest_rate, ".0") + " interest rate, your savings account will be worth " + format(doubled, ".2f") + " in " + format(years, ".1f") + " years.")