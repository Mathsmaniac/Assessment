"""
Made the text box and made sure the deleting worked
"""
import tkinter as tk
from tkinter import ttk


# Delete items from the textbox
def delete_selected():
    # Delete selected items from the actual list
    for i in listbox.curselection():
        test_list.pop(i)
    # Remake the list
    go_listbox()


# Add items to the listbox
def go_listbox():
    listbox.delete(0, "end")
    for item in test_list:
        listbox.insert('end', item)


# Root for testing
root = tk.Tk()

# Listbox component
listbox = tk.Listbox(root)
listbox.grid(row=0, column=0)
# Scrollbar for the listbox
scroller = ttk.Scrollbar(root)
scroller.grid(row=0, column=0, sticky="n, e, s")
# Set up scrolling function
listbox.config(yscrollcommand=scroller.set)
scroller.config(command=listbox.yview)
# Test data for the list
test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Initialise list
go_listbox()
# Button to delete items from listbox
item_delete_button = ttk.Button(root, text="Delete",
                                command=lambda: delete_selected())
item_delete_button.grid(row=0, column=1)

tk.mainloop()
