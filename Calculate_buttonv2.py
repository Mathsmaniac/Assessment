"""
In this version, I made the final results
"""
import tkinter as tk
from tkinter import ttk


# Make the storage class
class Item:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        self.value = amount/price


# Final top level
class LastTopLevel(tk.Toplevel):
    def __init__(self, parent, first_part, second_part):
        super().__init__(parent)
        # Declare style
        self.configure(background="#97dbe5")
        self.title("Final summary")
        s.configure("TLabel", background="#02fa82")
        s.configure("TFrame", background="#02fa82")
        s.configure("MainFrame.TFrame", borderwidth=5, relief="ridge")
        # Frame for results
        self.result_frame = ttk.Frame(self, style="MainFrame.TFrame")
        self.result_frame.grid(row=0, column=0)
        # First and second part of response
        self.first_part = first_part
        self.second_part = second_part
        # Button to make it go away
        self.self_destruct = ttk.Button(self.result_frame, text="Got It!",
                                        command=lambda: self.destroy())
        self.self_destruct.grid(row=4, column=0, padx=10, pady=10)
        # Title label
        ttk.Label(self.result_frame, text="Final Results!",
                  font=("Ariel", 15)).grid(row=0, column=0)
        # Labels for result
        ttk.Label(self.result_frame,
                  text=self.first_part).grid(row=2, column=0)
        ttk.Label(self.result_frame,
                  text=self.second_part).grid(row=3, column=0)
        # Give window focus
        self.focus()
        # Make it stay on the window
        self.grab_set()


# Make an easy storing function
def store(name, amount, price):
    name = Item(name, amount, price)
    items.append(name)


# Getting data from specified object
def takeaway(item_):
    returner = []
    for att in vars(item_).values():
        returner.append(att)
    return returner


# Make the result
def make_result():
    if not items:
        makeerror(calculate_error, "Please enter some items!")
        return
    # Sort into out and in of price range
    outs = []
    ins = []
    for result in items:
        if result.price > price_range:
            outs.append(result)
        else:
            ins.append(result)
    # Sort out the ones that are out of the price range and make the response
    # Based on how many there are
    if len(outs) < 1:
        first_part = ""
    elif len(outs) == 1:
        best_out = [outs[0]]
        first_part = f"The best buy is {best_out[0].amount}{unit} of " \
            f"{best_out[0].name}, however this is out of your price" \
            f" range\n"
    else:
        first_part = ""
        best_out = [outs[0]]
        for item in outs[1:]:
            if item.value > best_out[0].value:
                best_out.clear()
                best_out.append(item)
            elif item.value == best_out[0].value:
                best_out.append(item)
            else:
                pass
            first_part = f"The best buy is"
            for out in best_out:
                first_part += f" {out.amount}{unit} of {out.name} and"
            first_part = first_part[:-4]
            if len(best_out) > 1:
                first_part += ", with the same value for money, " \
                            "however these are out of your price range.\n"
            else:
                first_part += "however, this is out of you price range"
    # Sort out the ones that are inside the price range
    # And make the response based on how many there are
    if len(ins) < 1:
        second_part = ""
    elif len(ins) == 1:
        best_in = [ins[0]]
        second_part = f"The best buy in your price range is" \
                      f" {best_in[0].amount}{unit} of {best_in[0].name}"
    else:
        best_in = [ins[0]]
        for item in ins[1:]:
            if item.value > best_in[0].value:
                best_in.clear()
                best_in.append(item)
            elif item.value == best_in[0].value:
                best_in.append(item)
            else:
                pass
        second_part = f"The best buy in your price range is"
        for inner in best_in:
            second_part += f" {inner.amount}{unit} of {inner.name} and"
        second_part = second_part[:-4]
        if len(best_in) > 1:
            second_part += ", with the same value for money\n"
    try:
        if best_out[0].value <= best_in[0].value:
            first_part = ""
    except UnboundLocalError:
        pass
    # Make the final top level
    LastTopLevel(root, first_part, second_part)


# Makes the error message
def makeerror(label, error_message):
    label.configure(text=error_message)
    # Hides the text
    root.after(5000, lambda: label.configure(text=""))


# Root for testing
root = tk.Tk()
# Declare style
s = ttk.Style()
s.configure("Error.TLabel", foreground="red")
# List
items = []
# Dummy data for testing
unit = "g"
store("Salty Leave", 200, 400)
# store("School Tardy", 300, 600)
# store("Salty Leave", 100, 200)
price_range = 1000
# Error for calculate button
calculate_error = ttk.Label(root, style="Error.TLabel")
calculate_error.grid(row=0, column=0)
# Calculate button
calculate = ttk.Button(root, text="Calculate!", command=lambda: make_result())
calculate.grid(row=1, column=0)
tk.mainloop()
