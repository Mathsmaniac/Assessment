import tkinter as tk
from tkinter import ttk


def is_blank(input_):
    if input_.isspace() or input_ == "":
        return True
    else:
        return False


# Check int function
def check_int(to_check):
    # Uses isinstance to determine variable type
    if isinstance(to_check, int):
        return False
    # returns true if it hasn't returned false
    return True


def check():
    if is_blank(price_range_box.get()):
        makeerror("This can't be blank!")
    elif check_int(price_range_box.get()):
        makeerror("This has to be a number!")
    else:
        root.deiconify()
        new_window.destroy()


def makeerror(error_message):
    price_range_error.configure(text=error_message)
    # Hides the text
    root.after(5000, lambda: price_range_error.configure(text=""))


root = tk.Tk()
new_window = tk.Toplevel()
new_window.configure(background="#97dbe5")
new_window.geometry("400x400")
s = ttk.Style()
s.configure("PadFrame.TFrame", borderwidth=0, relief="", background="#97dbe5")
s.configure("Error.TLabel", foreground="red", background="#02fa82")
s.configure("TFrame", borderwidth=5, relief="ridge", background="#02fa82")
padder = ttk.Frame(new_window, width=100, height=100, style="PadFrame.TFrame")
padder.grid(row=0, column=0)
info_frame = ttk.Frame(new_window, padding=15)
info_frame.grid(row=1, column=1)
price_range_error = ttk.Label(info_frame, text="", style="Error.TLabel")
price_range_error.grid(row=0, column=1)
price_range_box = ttk.Entry(info_frame, width=9)
price_range_box.grid(row=1, column=1)
check_button = ttk.Button(info_frame, text="Ok, go!", command=lambda: check())
check_button.grid(row=2, column=1)
root.withdraw()
root.mainloop()
