# Converting Celsius to Fahrenheit

# Create the variable celsius
celsius = float(input("Enter temperature in Celsius: "))

# Now convert that variable (celsius) to Fahrenheit 

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius} °C is equal to {fahrenheit:.2f} °F")


student = ('Alice', 20, 'Data Analytics', 3.5, True)
           
print(student)
print(f"Name : {student[0]}")
print(f"Age : {student[1]}")
print(f"Major : {student[2]}")
print(f"GPA : {student[3]}")
print(f"Active : {student[4]}")
print(f"Length : {len(student)}")

# count (x)
t = (1,2,2,3,2)
print(t.count(2))

print(t.index(2))