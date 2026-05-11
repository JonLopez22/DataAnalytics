# Net Worth Calculator but with user input

# Assets
savings = float(input("Enter your savings amount: $"))
car_value = float(input("Enter the current value of your car: $"))
investments = float(input("Enter the current value of your investments: $"))
total_assets = savings + car_value + investments

# Debts
car_loan = float(input("Enter the current balance of your car loan: $"))
credit_card = float(input("Enter the current balance of your credit card: $"))
total_debts = car_loan + credit_card

# Net Worth
net_worth = total_assets - total_debts

print(f"\nYour total assets are: ${total_assets:.2f}")
print(f"Your total debts are: ${total_debts:.2f}")
print(f"Your net worth is: ${net_worth:.2f}")

# Observations:
# 1. input()( always returns a string, so float() is required before doing any math, forgetting this crashes the program.
# 2. If the user types letters instead of a number, the program will crash with a ValueError
# 3. If the user types a negative number, the program won't catch it, a negative savings amount doesn't make sense