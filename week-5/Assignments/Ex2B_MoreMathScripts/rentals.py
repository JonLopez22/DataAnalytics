# 6. There are X people going on a tour. Charter vans seat 15 passengers each. 
# Vans cost $250 per day to rent (including the driver’s pay). 
# How many vans do you need? How much will it cost to rent vans? What is the cost if you split it per person?

import math

num_tourists = int(input("Enter number of tourists: "))
van_capacity = 15
van_cost = 250

vans_needed = math.ceil(num_tourists / van_capacity)
total_cost = vans_needed * van_cost
cost_per_person = math.ceil(total_cost / num_tourists)

print(f"Number of vans needed: {vans_needed}")
print(f"Total cost to rent vans: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

# a) How much money did your script say you had to charge per person? $19.00
# b) If you multiply that out, how much did you collect? $760
# c) How much were the vans? $750
# d) Why do you have leftover money? Because we rounded up the cost per person to the nearest dollar, we collected more money than the total cost of the vans.