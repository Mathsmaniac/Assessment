"""
Made the Drop down list widget. Reasonably simple so no developing is needed
"""
import tkinter as tk
from tkinter import ttk


# Simple root for testing
root = tk.Tk()
# Simple top level for testing purposes
mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0)
# Options for the drop down list
options = ["mg", "g", "kg", "st", "oz", "lb", "t", "mL", "L"]
# Declare style
s = ttk.Style()
s.configure("TMenubutton", background="#009947")
# Variable for item selected
selected = tk.StringVar()
# Drop down list widget
drop = ttk.OptionMenu(mainframe, selected, options[1], *options,
                      command=lambda event: print(selected.get()))
drop.grid(row=1, column=2, sticky="W")
tk.mainloop()
