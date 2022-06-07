import tkinter as tk
from tkinter import ttk


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


def check():
    price = price_box.get()
    # Check if input is blank
    if is_blank(price):
        makeerror(price_error, "This can't be blank!")
    # Check if input is int
    elif check_int(price):
        makeerror(price_error, "This has to be a number!")
    else:
        # Print input if fine for testing
        print(price)


# Makes the error message
def makeerror(label, error_message):
    label.configure(text=error_message)
    # Hides the text
    root.after(5000, lambda: label.configure(text=""))


root = tk.Tk()

# Declare style
s = ttk.Style()
s.configure("Error.TLabel", foreground="red")

# Box for price of item
price_box = ttk.Entry(root)
price_box.grid(row=1, column=1)
# Error for price of item box
price_error = ttk.Label(root, style="Error.TLabel")
price_error.grid(row=0, column=1)
# Info label for price of item box
price_label = ttk.Label(root, text="Price: $")
price_label.grid(row=1, column=0, sticky="e")
# Enter keybind for ease of testing
price_box.bind("<Return>", lambda event: check())
tk.mainloop()
