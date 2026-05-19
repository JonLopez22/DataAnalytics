class Restaurant:
    '''Represents a restaurant with a name and food type.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


# Creating instances (3)
rest_1 = Restaurant("Carmine's", "Italian")
rest_2 = Restaurant("Xi'an Famous Foods", "Chinese")
rest_3 = Restaurant("Los Tacos No. 1", "Mexican")

# Time to call it
rest_1.describe_rest()
rest_1.rest_open()

rest_2.describe_rest()
rest_2.rest_open()

rest_3.describe_rest()
rest_3.rest_open()