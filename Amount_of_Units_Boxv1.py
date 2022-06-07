"""
A simple box to get the
"""
import tkinter as tk
from tkinter import ttk


# function that gets input from the box and does stuff with it
def push_info():
    units = amount_of_units_box.get()
    amount_of_units_box.delete(0, "end")
    # If not blank, print data for testing purposes
    if is_blank(units):
        makeerror(amount_of_units_error, "This can't be blank")
    elif check_int(units):
        makeerror(amount_of_units_error, "This has to be an integer!")
    else:
        print(units)


# Makes the error message
def makeerror(label, error_message):
    label.configure(text=error_message)
    # Hides the text
    root.after(5000, lambda: label.configure(text=""))


# Not blank function
def is_blank(input_):
    if input_.isspace() or input_ == "":
        return True
    else:
        return False


# Check int function
def check_int(to_check):
    try:
        # Returns false if the code works, if it doesn't the try kicks in
        int(to_check)
        return False
    except ValueError:
        return True


# Make frame for testing
root = tk.Tk()
mainframe = ttk.Frame(root)
mainframe.grid(row=1, column=1)
# Declare style
s = ttk.Style()
s.configure("Error.TLabel", foreground="red")
# Box for amount of units
amount_of_units_box = ttk.Entry(mainframe, width=7)
amount_of_units_box.grid(row=1, column=0, sticky="w")
# Error label for amount of units
amount_of_units_error = ttk.Label(mainframe, style="Error.TLabel")
amount_of_units_error.grid(row=0, column=0)
# Enter keybind for testing purposes
amount_of_units_box.bind("<Return>", lambda event: push_info())
tk.mainloop()
