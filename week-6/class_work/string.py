#1 creat a string

text = "Pyhton"

#2 indexing (positive and negative)
print("First character:", text[0])
print("Last character:", text[-1])

#3 Slicing

print("First three characters:", text[0:3])
print("From index 2 to end:", text[2:])
print("Every second character:", text[::2])

#4 Iteration
print("Characters in string:")
for char in text:
    print(char, end=" ")
print()

#5 Membership testing
print("'Py' in text?" "Py" in text) 
print("'Java' in text?", "Java" in text)

#6 Length of string
print("Length of string:", len(text))

#7 Concatenation and repetition 
print("Concatenation:", text + "3.11")
print("Repetition:", text * 2)

#8 Immutability demonstration
try:
    text[0] = "J" 
except TypeError as e:
    print("Strings are immutable:", e)