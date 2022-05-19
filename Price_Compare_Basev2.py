"""
Added StorageClassv2.py to the base program,
Integrated it in so that the data entered into the box goes into the system
prints out the data each time for testing purposes
"""
import tkinter as tk
from tkinter import ttk


# Make the class
class Item:
    def __init__(self, name):
        self.name = name


# Make an easy storing function
def store(name):
    name = Item(name)
    items.append(name)


# Getting data from specified object
def takeaway(item_):
    returner = []
    for att in vars(item_).values():
        returner.append(att)
    return returner


# function that gets input from the box and does stuff with it
def push_info():
    good = good_entry.get()
    good_entry.delete(0, "end")
    # Give focus to text box
    good_entry.focus_set()
    # Put data into storage system
    store(good)
    # Print all stuff in system for testing purposes
    print()
    for good_ in items:
        print(takeaway(good_))


# Declare Variables and lists
items = []
# Initialise mainframe, declare style
root = tk.Tk()
s = ttk.Style()
root.title("Price Compare Tool")
root.geometry("700x600")
root.configure(background="#97dbe5")
s.configure("TFrame", borderwidth=5, relief="ridge", background="#02fa82")
s.configure("PadFrame.TFrame", borderwidth=0, relief="", background="#97dbe5")
# Create frames
pad_frame = ttk.Frame(root, width=150, height=150, style="PadFrame.TFrame")
pad_frame.grid(row=0, column=0)
mainframe = ttk.Frame(root, padding="15")
mainframe.grid(row=1, column=1, sticky=("n", "w", "e", "s"))
# Create widgets
good_entry = ttk.Entry(mainframe, width=20)
good_entry.grid(row=0, column=0, sticky="n")
push_info_button = ttk.Button(mainframe, text="Add", command=push_info)
push_info_button.grid(row=1, column=0, sticky="s")
# Add enter key bind
good_entry.bind("<Return>", lambda event: push_info())
# Add padding to widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
items = []
tk.mainloop()
