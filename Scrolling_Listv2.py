"""
Used actual data from class format
"""
import tkinter as tk
from tkinter import ttk


# Getting data from specified object
def takeaway(item_):
    returner = []
    for att in vars(item_).values():
        returner.append(att)
    return returner


# Delete items from the textbox
def delete_selected():
    # Delete selected items from the actual list
    for i in listbox.curselection():
        items.pop(i)
    # Remake the list
    go_listbox()


def store(name, amount):
    name = Item(name, amount)
    items.append(name)


# Make the storage class
class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


# Add items to the listbox
def go_listbox():
    listbox.delete(0, "end")
    for item in items:
        listbox.insert('end', f"{takeaway(item)[1]}g of {takeaway(item)[0]}")


# Root for testing
root = tk.Tk()
# Listbox component
listbox = tk.Listbox(root, width=30)
listbox.grid(row=0, column=0)
# Scrollbar for the listbox
scroller = ttk.Scrollbar(root)
scroller.grid(row=0, column=0, sticky="n, e, s")
# Set up scrolling function
listbox.config(yscrollcommand=scroller.set)
scroller.config(command=listbox.yview)
# Test data for the listbox
items = []
store("Salty Leave", 90)
store("School Tardy", 500)
store("Comb over", 305)
# Initialise list
go_listbox()
# Button to delete items from listbox
item_delete_button = ttk.Button(root, text="Delete",
                                command=lambda: delete_selected())
item_delete_button.grid(row=0, column=1)

tk.mainloop()
