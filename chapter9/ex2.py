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

class User():
    def __init__(self,first_name,last_name):
        self.name =first_name
        self.lastname=last_name

    def describe_user(self):
        print(f"Welcome {self.name} {self.lastname}")

    def greet_user(self):
        print("Hello" " " + self.name)


user = User("Alis", "Jhones")
user.describe_user()
user.greet_user()
