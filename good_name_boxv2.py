"""
In this version, I added the functionality to press enter to push the input
Additionally, the text box clears when the input is given
"""
import tkinter as tk
from tkinter import ttk


# function that gets input from the box and does stuff with it
def push_info():
    item = good_entry.get()
    print(f"The user entered: {item}")
    good_entry.delete(0, "end")


# Initialise mainframe, declare style
root = tk.Tk()
s = ttk.Style()
root.title("Price Compare Tool")
root.geometry("700x600")
root.configure(background="#97dbe5")
s.configure("TFrame", borderwidth=5, relief="ridge", background="#02fa82")
s.configure("Padframe.TFrame", borderwidth=0, relief="", background="#97dbe5")
# Create frames
pad_frame = ttk.Frame(root, width=150, height=150, style="Padframe.TFrame")
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
