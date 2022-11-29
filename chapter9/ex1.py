class Restaurant():
    """A class representing a restaurant"""

    def __init__(self, name, cusisne_type):
        self.name = name.title()
        self.cusisne_type = cusisne_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"The restaurant name is {self.name} and cusisne is {self.cusisne_type}")

    def open_restaurant(self):
        print(f"{self.name} is open")


restaurant = Restaurant("Varduk", "Asian")
print(restaurant.name)
print(restaurant.cusisne_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
        