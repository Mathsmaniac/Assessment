"""
Added good_name_boxv3.py to the base program, changed it so it doesn't
print the output, because that's not what we want to do
We currently aren't doing anything with the output we get out,
this will be fixed in the next component
"""
import tkinter as tk
from tkinter import ttk


# function that gets input from the box and does stuff with it
def push_info():
    item = good_entry.get()
    good_entry.delete(0, "end")
    # Give focus to text box
    good_entry.focus_set()


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
tk.mainloop()
