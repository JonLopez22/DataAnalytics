class Restaurant:
    ''' Represents a restaurant with a name, food type, customer count, and ratings.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        count = int(input("How many customers served today? "))
        self.number_served += count

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            try:
                rating = int(input("Rate your experience 1-5 (5 = excellent): "))
                if 1 <= rating <= 5:
                    break
                else:
                    print("Please enter a whole number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a whole number between 1 and 5.")

        self.customer_ratings.append(rating)
        avg = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f"Your rating was {rating}. The average rating for {self.rest_name} is {avg:.1f}.")

rest_1 = Restaurant("Carmine's", "Italian")

rest_1.print_num_served()
rest_1.add_num_served()
rest_1.add_num_served()
rest_1.print_num_served()

rest_1.customer_rating()
rest_1.customer_rating()
rest_1.customer_rating()
rest_1.customer_rating()