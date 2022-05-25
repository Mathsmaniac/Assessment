"""
In this version I incorporated my function into a testing GUI
"""


import tkinter as tk
from tkinter import ttk


# Not blank function
def is_blank(input_):
    if input_.isspace() or input_ == "":
        return True
    else:
        return False


# Function for testing
def test_func():
    if is_blank(test_entry.get()):
        maketext()
    else:
        pass


# Shows the text
def maketext():
    error_label.configure(text="This can't be blank")
    root.after(5000, cleartext)


# Makes the text go away
def cleartext():
    error_label.configure(text="")


# Initialise test GUI
root = tk.Tk()
s = ttk.Style()
# Initialise style for warning label
s.configure("Error.TLabel", foreground="red")
# Make the label, it starts blank
error_label = ttk.Label(root, style="Error.TLabel")
error_label.grid(row=0, column=0, sticky=("s", "w"))
# Make the testing box
test_entry = ttk.Entry(root, width=20)
test_entry.grid(row=1, column=0, sticky="n")
test_entry.bind("<Return>", lambda event: test_func())
root.mainloop()
