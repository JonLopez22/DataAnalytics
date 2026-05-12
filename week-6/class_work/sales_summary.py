# get some input
name = input("Associates name: ")
region = input("Store's region: ")
units = int(input("Units sold: "))
price = float(input("Price per unit $: "))

# Define

def sales_summary(name, region, units, price):
    revenue = units * price
    bonus = revenue * 0.10
    return revenue, bonus

# Calling the function
revenue, bonus = sales_summary(name, region, units, price)

# lets print
print(f"""
Associate : {name}
Region : {region}
Units sold: {units}
Unit price: ${price:.2f}
------------------------------
Total revenue: ${revenue:.2f}
Pefromance bonus (10%): ${bonus:.2f}
-----------------------------------------
""")