total = 0
count = 0

print("Enter positive numbers one at a time.")
print("Enter a negative number to stop.")

number = float(input("Enter a number: "))

while number >= 0:
    total += number
    count += 1
    number = float(input("Enter a number: "))

print(f"\nNumbers entered: {count}")
print(f"Sum              : {total:.2f}")