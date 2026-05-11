# 1. Choose one or more of the above exercises, and figure out how to re-write the print output as an f-string.

# Net Worth (before)

# Assets
savings = 5000
car_value = 12000
investments = 3000
total_assets = savings + car_value + investments

# Debts
car_loan = 8000
credit_card = 1500
total_debts = car_loan + credit_card

net_worth = total_assets - total_debts

print("Your total assets are " + str(total_assets))
print("Your total debts are " + str(total_debts))
print("Your net worth is " + str(net_worth))

print("-" * 30)
# Net Worth (after)

print(f"Your total assets are ${total_assets:.2f}")
print(f"Your total debts are ${total_debts:.2f}")
print(f"Your net worth is ${net_worth:.2f}")

print("-" * 30)

# rule_of_72 (before)
savings = 5000
interest_rate = 0.06   # 6%

years = 72 / (interest_rate * 100)
doubled = savings * 2

print("Your current savings is " + str(savings) + ".")
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be worth " 
      + format(doubled, ".2f") + " in " + format(years, ".1f") + " years")

# rule_of_72 (after)
# BEFORE
print("Your current savings is $" + str(savings) + ".")
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be worth $" + format(doubled, ".2f") + " in " + format(years, ".1f") + " years.")
print("-" * 30)
# AFTER (much cleaner!)
print(f"Your current savings is ${savings}.")
print(f"At a {interest_rate:.0%} interest rate, your savings account will be worth ${doubled:.2f} in {years:.1f} years.")