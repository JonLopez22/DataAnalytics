# 3. Federal taxes are 23% of your salary every month. You make X amount of money. How much is withheld for taxes?

salary = float(input("Enter your monthly salary: "))
tax_rate = 0.23
tax_withheld = salary * tax_rate
take_home = salary - tax_withheld

print(f"Your monthly salary is ${salary:.2f}.")
print(f"Federal taxes withheld: ${tax_withheld:.2f}.")
print(f"Your take-home pay after taxes is: ${take_home:.2f}.")