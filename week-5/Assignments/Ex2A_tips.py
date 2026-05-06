# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
# print("The total amount due is: $" + str(total_due))

# 2. str() is used to conver something into text. Its being used here to conver the total_due variable into text so that it can be concatenated with the rest of the string.

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))