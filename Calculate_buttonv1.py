"""
In this version, I made a button to open a window
The window can't be closed until it goes away
It also has a button to close the window
"""
import tkinter as tk
from tkinter import ttk


# Final top level
class LastTopLevel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Final summary")
        self.focus()
        self.grab_set()
        self.result_label = ttk.Label(self, text="<Results go here>")
        self.result_label.grid(row=0, column=0)
        self.self_destruct = ttk.Button(self, text="Got It!",
                                        command=lambda: self.go_away())
        self.self_destruct.grid(row=1, column=0, padx=10, pady=10)

    def go_away(self):
        self.destroy()


def make_result():
    LastTopLevel(root)


root = tk.Tk()
calculate = ttk.Button(root, text="Calculate!", command=lambda: make_result())
calculate.grid(row=0, column=0)

tk.mainloop()
