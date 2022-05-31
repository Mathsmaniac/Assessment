import tkinter as tk
from tkinter import ttk


root = tk.Tk()
new_window = tk.Toplevel()
options = ["Unit:", "mg", "g", "kg", "st", "oz", "lb", "t", "mL", "L"]

selected = tk.StringVar()
drop = ttk.OptionMenu(new_window, selected, *options)
drop.grid(row=1, column=1)
tk.mainloop()
