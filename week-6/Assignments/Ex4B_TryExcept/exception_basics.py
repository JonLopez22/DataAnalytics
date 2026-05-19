try: 
    num = int("hello")
except ValueError:
    print("ValueError: Can't convert that string to an integer.")
else:
    print(f"Converted successfully: {num}")
finally:
    print("Let's try another one...\n")

try:
    result = banana
except NameError:
    print("NameError: That variable doesn't exist yet.")
else:
    print(result)
finally:
    print("Let's try another one...\n")

try:
    total = "5" + 5
except TypeError:
    print("TypeError: Can't add a string and an integer directly.")
else:
    print(total)
finally:
    print("Let's try another one...\n")

try: 
    eval("if if if")
except SyntaxError:
    print("SyntaxError: That's not valid Python syntax.")
else:
    print("No syntax error found.")
finally:
    print("Let's try another one...\n")