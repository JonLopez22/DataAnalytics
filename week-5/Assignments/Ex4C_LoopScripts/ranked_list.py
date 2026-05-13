favorites = ["tacos", "ramen", "jerk chicken", "injera", "pierogi"]

# using enumerate()
for index, item in enumerate(favorites, start=1):
    if index == 1:
        print(f"{index}. {item} <- top pick!")
    else:
        print(f"{index}. {item}")


# Bounus - Reversed order
print("\nReversed list:")
reversed_list = list(reversed(favorites))
for index, item in enumerate(reversed_list, start=1):
    if index == 1:
        print(f"{index}. {item} <- top pick!")
    else: 
        print(f"{index}. {item}")