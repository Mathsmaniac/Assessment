"""
Added and merged Price_Range_boxv3 into the program
"""
import tkinter as tk
from tkinter import ttk


# Make the class
class Item:
    def __init__(self, name):
        self.name = name


# Check int function
def check_int(to_check):
    try:
        # Returns false if the code works, if it doesn't the try kicks in
        int(to_check)
        return False
    except ValueError:
        return True


# Not blank function
def is_blank(input_):
    if input_.isspace() or input_ == "":
        return True
    else:
        return False


# Makes the error message
def makeerror(label, error_message):
    label.configure(text=error_message)
    # Hides the text
    root.after(5000, lambda: label.configure(text=""))


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


def check():
    price_range_box.focus_set()
    if is_blank(price_range_box.get()):
        makeerror(price_range_error, "This can't be blank!")
    elif check_int(price_range_box.get()):
        makeerror(price_range_error, "This has to be an integer!")
    else:
        root.deiconify()
        good_entry.focus_set()
        price_range.set(price_range_box.get())
        price_range_mainlabel.configure(text=f"Your price range i"
                                             f"s ${price_range.get():.2f}")
        new_window.destroy()


# function that gets input from the box and does stuff with it
def push_info():
    good = good_entry.get()
    good_entry.delete(0, "end")
    # Give focus to text box
    good_entry.focus_set()
    # If not blank, put data into storage system
    if is_blank(good):
        makeerror(error_label, "This can't be blank")
    else:
        store(good)
    # Print all stuff in system for testing purposes
    print()
    for good_ in items:
        print(takeaway(good_))


# Declare Variables and lists
items = []
# Initialise mainframe and toplevels
root = tk.Tk()
root.title("Price Compare Tool")
root.geometry("700x600")
root.configure(background="#97dbe5")
new_window = tk.Toplevel(root)
new_window.configure(background="#97dbe5")
new_window.geometry("400x400")

# Declare style
s = ttk.Style()
s.configure("PadFrame.TFrame", borderwidth=0, relief="", background="#97dbe5")
s.configure("Error.TLabel", foreground="red", background="#02fa82")
s.configure("TFrame", borderwidth=5, relief="ridge", background="#02fa82")
s.configure("TLabel", background="#02fa82")

# Declare variables
price_range = tk.IntVar()

# Create frames
pad_frame = ttk.Frame(root, width=150, height=150, style="PadFrame.TFrame")
pad_frame.grid(row=0, column=0)
mainframe = ttk.Frame(root, padding="15")
mainframe.grid(row=1, column=1, sticky=("n", "w", "e", "s"))

# Create widgets
error_label = ttk.Label(mainframe, style="Error.TLabel")
error_label.grid(row=1, column=0, sticky=("s", "w"))
good_entry = ttk.Entry(mainframe, width=20)
good_entry.grid(row=2, column=0, sticky="n")
push_info_button = ttk.Button(mainframe, text="Add", command=push_info)
push_info_button.grid(row=3, column=0, sticky="s")
padder = ttk.Frame(new_window, width=100, height=100, style="PadFrame.TFrame")
padder.grid(row=0, column=0)
info_frame = ttk.Frame(new_window, padding=15)
info_frame.grid(row=1, column=1)
price_range_error = ttk.Label(info_frame, text="", style="Error.TLabel")
price_range_error.grid(row=0, column=1)
price_range_box = ttk.Entry(info_frame, width=9)
price_range_box.grid(row=1, column=1)
price_range_label = ttk.Label(info_frame, text="Price range:  $")
price_range_label.grid(row=1, column=0)
check_button = ttk.Button(info_frame, text="Ok, go!", command=lambda: check())
check_button.grid(row=2, column=0, columnspan=2)
check_button.grid_configure(padx=20, pady=5)
price_range_mainlabel = ttk.Label(mainframe, text="")
price_range_mainlabel.grid(row=0, column=0)

# Add enter key bind
good_entry.bind("<Return>", lambda event: push_info())
price_range_box.bind("<Return>", lambda event: check())
# Add padding to widgets
push_info_button.grid_configure(padx=5, pady=5)

# Set focus to first widget
price_range_box.focus_set()

root.withdraw()
tk.mainloop()
