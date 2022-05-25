"""
Added Not_Blankv3 to the base program,
"""
import tkinter as tk
from tkinter import ttk


# Make the class
class Item:
    def __init__(self, name):
        self.name = name


# Not blank function
def is_blank(input_):
    if input_.isspace() or input_ == "":
        return True
    else:
        return False


# Shows the text
def makeerror():
    error_label.configure(text="This can't be blank")
    # Hides the text
    root.after(5000, lambda: error_label.configure(text=""))


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
    # If not blank, put data into storage system
    if is_blank(good):
        makeerror()
    else:
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
s.configure("Error.TLabel", foreground="red", background="#02fa82")


# Create frames
pad_frame = ttk.Frame(root, width=150, height=150, style="PadFrame.TFrame")
pad_frame.grid(row=0, column=0)
mainframe = ttk.Frame(root, padding="15")
mainframe.grid(row=1, column=1, sticky=("n", "w", "e", "s"))

# Create widgets
error_label = ttk.Label(mainframe, style="Error.TLabel")
error_label.grid(row=0, column=0, sticky=("s", "w"))
good_entry = ttk.Entry(mainframe, width=20)
good_entry.grid(row=1, column=0, sticky="n")
push_info_button = ttk.Button(mainframe, text="Add", command=push_info)
push_info_button.grid(row=2, column=0, sticky="s")

# Add enter key bind
good_entry.bind("<Return>", lambda event: push_info())

# Add padding to widgets
push_info_button.grid_configure(padx=5, pady=5)

# Set focus to first widget
good_entry.focus_set()

tk.mainloop()
