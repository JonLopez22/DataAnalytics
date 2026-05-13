bank_balance = 500.00
savings_goal = 2000.00
weekly_savings = 150.00

while bank_balance < savings_goal:
    bank_balance += weekly_savings

    if bank_balance >= savings_goal * 0.75:
        treat = 10.00
        bank_balance -= treat
        print(f"So close! After treating myself, my balance is up to ${bank_balance:.2f}")
    elif bank_balance >= savings_goal * 0.50:
        print(f"Almost there! This week my balance is up to ${bank_balance:.2f}")
    else:
        print(f"This week my balance increased to ${bank_balance:.2f}")

print(f"Goal met! My current balance is ${bank_balance:.2f}")