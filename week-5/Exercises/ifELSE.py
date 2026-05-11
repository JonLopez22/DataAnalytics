day1 = "Monday"
day2 = "Tuesday"
day3 = "Wednesday"
day4 = "Thursday"
day5 = "Friday"
day6 = "Saturday"
day7 = "Sunday"

day = int(input("Enter a number between 1 and 7: "))

if day >= 1 and day <= 7:
    if day == 1:
        print("The day is", day1)
    elif day == 2:
        print("The day is", day2)
    elif day == 3:
        print("The day is", day3)
    elif day == 4:
        print("The day is", day4)
    elif day == 5:
        print("The day is", day5)
    elif day == 6:
        print("The day is", day6)
    elif day == 7:
        print("The day is", day7)
else:
    print(f"Error: {day} is not a number between 1 and 7.")