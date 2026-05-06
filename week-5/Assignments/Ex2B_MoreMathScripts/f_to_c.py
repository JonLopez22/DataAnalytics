# 1. How do you convert a temperature from Fahrenheit to Celsius?

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius")