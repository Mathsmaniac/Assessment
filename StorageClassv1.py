"""
Simply made the class, and a method to enter data into it
"""


# Make the class
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Make an easy storing function
def store(name, price):
    name = Item(name, price)
    items.append(name)


items = []
while True:
    # Entering data for testing purposes
    store(input("Name: "), input("Price: "))
    print()
    # Print everything for testing purposes
    for item in items:
        print(f"Name: {item.name}, Price: {item.price}")
