import tkinter as tk
from tkinter import ttk


def push_info():
    print(f"The user entered: {good.get()}")


root = tk.Tk()
s = ttk.Style()
root.title("Price Compare Tool")
root.geometry("700x600")
root.configure(background="#97dbe5")
s.configure("TFrame", borderwidth=5, relief="ridge", background="#02fa82")
s.configure("Padframe.TFrame", borderwidth=0, relief="", background="#97dbe5")
pad_frame = ttk.Frame(root, width=150, height=150, style="Padframe.TFrame")
pad_frame.grid(row=0, column=0)
mainframe = ttk.Frame(root, padding="15")
mainframe.grid(row=1, column=1, sticky=("n", "w", "e", "s"))
good = StringVar()
good_entry = ttk.Entry(mainframe, width=20, textvariable=good)
good_entry.grid(row=0, column=0, sticky="n")
push_info_button = ttk.Button(mainframe, text="Add", command=push_info)
push_info_button.grid(row=1, column=0, sticky="s")
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
tk.mainloop()
