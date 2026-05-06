# Description: Working with tuples and sets
# Author: Jonathan Lopez

candy_types = ("Skittles", "Starburst", "Jolly Ranchers")
flavors = ("watermelon", "strawberry", "mango")

candy_combos = set()
candy_combos.add(candy_types[0] + " " + flavors[1])
candy_combos.add(candy_types[1] + " " + flavors[0])
candy_combos.add(candy_types[2] + " " + flavors[2])

print("Today's candy options include:")
print(candy_combos)