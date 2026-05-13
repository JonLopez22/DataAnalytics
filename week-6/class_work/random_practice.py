import random
# 1 Random integer between a and b (inclusive)
print("randint(1, 10):", random.randint(1, 10))

# 2 Random float between 0.0 and 1.0
print("random():", random.random())

# 3 Random single element from a sequence
fruits = ["apple", "banana", "cherry"]
print("choice(fruits):", random.choice(fruits))

# 4 List of k random elements (with replacement) 
print("choice(fruits, k=3):", random.choices(fruits, k=3))

# 5 List of k unique random elements (without replacement)
print("sample(fruits, k=2):", random.sample(fruits, k=2))

# 6 shuffles a list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("shuffled numbers:", numbers)