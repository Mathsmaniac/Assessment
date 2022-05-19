"""
Added a function to take stuff out of the class easily, in list form
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


# Getting data from specified object
def takeaway(item_):
    returner = []
    for att in vars(item_).values():
        returner.append(att)
    return returner


items = []
while True:
    # Entering data for testing purposes
    store(input("Name: "), input("Price: "))
    print()
    # Print everything for testing purposes
    for item in items:
        print({(takeaway(item))})
