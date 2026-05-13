sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShwan Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]
total_sales = 0

for name, region, total in sales_data:
    print(f"{name} ({region}): ${total:,.2f}")
    if total > 5000:
        print(" ^ Top performer!")
        total_sales += total

# BONUS
print("f\nTotal sales across all employees: ${total_sales:,.2f}")