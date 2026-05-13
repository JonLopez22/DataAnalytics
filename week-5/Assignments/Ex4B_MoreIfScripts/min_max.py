a = 42
b = 17
c = 89

# Finding the minimum
if a <= b and a <= c:
    smallest = a 
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Finding the maximum
if a >= b and a >= c:
    largest = a 
elif b >= a and b >= c:
    largest = b 
else:
    largest = c 

print(f"The smallest value is {smallest}")
print(f"The largest value is {largest}")