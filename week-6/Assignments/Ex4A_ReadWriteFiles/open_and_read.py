f = open('about_me.txt', 'r')

content = f.read(50)
more_content = f.read(50)
f.close()

f = open('about_me.txt', 'r')

first_chunk = f.readline(10)
rest_of_line = f.readline()

for i in range(1, 5):
    print(f.readline())

f.close()

f = open('about_me.txt', 'r')

first_50 = f.read(50)

lines_list = []
for i in range(4):
    lines_list.append(f.readline())

    rest_as_list = f.readlines(100)

f.close()

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {lines_list}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {rest_as_list}")