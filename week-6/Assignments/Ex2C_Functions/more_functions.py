# Displaying mail label
def display_mailing_label(name, address, city, state, zip):
    print(f"{name}")
    print(f"{address}")
    print(f"{city}, {state} {zip}")
    print()

display_mailing_label('Jonathan Lopez', '2244 Who St', 'New York', 'NY', '11385')
display_mailing_label('Jane Smith', '456 Oak Ave', 'Brooklyn', 'NY', '11201')

# Add numbers
def add_numbers(*args):
    result = sum(args)
    equation = ' + '.join(str(n) for n in args)
    print(f"{equation} = {result}")

add_numbers(5)
add_numbers(10, 20)
add_numbers(1, 2, 3, 4, 5)

# Displaying a receipt
def display_receipt(total_due, amount_paid):
    print(f"Total Due:   ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due:   ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining balance to be paid:  ${balance:.2f}")
        print()

display_receipt(50.00, 60.00)
display_receipt(50.00, 50.00)
display_receipt(50.00, 30.00)