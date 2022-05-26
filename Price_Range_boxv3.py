"""
In this version I simply added some information labels to the toplevel
"""
import tkinter as tk
from tkinter import ttk


# Checks if input is blank
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


# Makes sure the input is not blank and is an int
# If all is well, it destroys the toplevel and shows the main window
# If all is not well, it displays the correct error message
def check():
    price_range_box.focus_set()
    if is_blank(price_range_box.get()):
        makeerror(price_range_error, "This can't be blank!")
    elif check_int(price_range_box.get()):
        makeerror(price_range_error, "This has to be an integer!")
    else:
        root.deiconify()
        new_window.destroy()


# Makes the error message
def makeerror(label, error_message):
    label.configure(text=error_message)
    # Hides the text
    root.after(5000, lambda: label.configure(text=""))


# Initalise root and toplevel
root = tk.Tk()
new_window = tk.Toplevel()
new_window.configure(background="#97dbe5")
new_window.geometry("400x400")
# Declare styles
s = ttk.Style()
s.configure("PadFrame.TFrame", borderwidth=0, relief="", background="#97dbe5")
s.configure("Error.TLabel", foreground="red", background="#02fa82")
s.configure("TFrame", borderwidth=5, relief="ridge", background="#02fa82")
s.configure("TLabel", background="#02fa82")
# Make and grid widgets
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
# User can press enter to submit info
price_range_box.bind("<Return>", lambda event: check())
# Starts with focus on the entry widget
price_range_box.focus_set()
# Hides the main root until it is shown by the check function
root.withdraw()
root.mainloop()
