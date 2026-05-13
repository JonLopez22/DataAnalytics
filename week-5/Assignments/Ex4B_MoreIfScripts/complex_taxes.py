# step 1 - calculate gross pay weekly
pay_rate = 17.30
hours_worked = 45
filing_status = 'single'

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_pay = pay_rate * 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_weekly_pay = regular_pay + overtime_pay
else:
    gross_weekly_pay = pay_rate * hours_worked

# Step 2: Lets estimate gross pay annually
annual_gross = gross_weekly_pay * 52

# Step 3: Determine tax rate by filiing status and income
if filing_status == 'single':
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == 'joint':
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else: 
        tax_rate = 0.20
else: 
    tax_rate = 0.00
    print("Unrecognized filing status.")

# Step 4 Calculate weekly tax and net pay
weekly_tax = gross_weekly_pay * tax_rate
net_pay = gross_weekly_pay - weekly_tax

# Step 5 Print all results
print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_weekly_pay:.2f}")
print(f"Your estimate annual gross is ${annual_gross:,.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${weekly_tax:.2f}")
print(f"Your net pay is {net_pay:.2f}")