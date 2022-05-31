"""
Made program object and class orientated
Fixed object destroyed label change bug
"""
import tkinter as tk
from tkinter import ttk


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.price_range = tk.IntVar()
        # Declare style
        s = ttk.Style()
        s.configure("PadFrame.TFrame", borderwidth=0, relief="",
                    background="#97dbe5")
        s.configure("Error.TLabel", foreground="red", background="#02fa82")
        s.configure("TFrame", borderwidth=5, relief="ridge",
                    background="#02fa82")
        s.configure("TLabel", background="#02fa82")
        # Configure window
        self.title("Price Compare Tool")
        self.geometry("700x600")
        self.configure(background="#97dbe5")
        # Padding frame
        self.pad_frame = ttk.Frame(self, width=150, height=150,
                                   style="PadFrame.TFrame")
        self.pad_frame.grid(row=0, column=0)
        # Main frame
        self.mainframe = ttk.Frame(self, padding="15")
        self.mainframe.grid(row=1, column=1, sticky=("n", "w", "e", "s"))
        # Error label
        self.error_label = ttk.Label(self.mainframe, style="Error.TLabel")
        self.error_label.grid(row=1, column=1, sticky=("s", "w"))
        # Entry box for good name with enter key binding
        self.good_entry = ttk.Entry(self.mainframe, width=20)
        self.good_entry.grid(row=2, column=1, sticky="n")
        self.good_entry.bind("<Return>", lambda event: self.push_info())
        # Info label
        self.good_entry_info = ttk.Label(self.mainframe, text="Item name: ")
        self.good_entry_info.grid(row=2, column=0)
        # Button to store info
        self.push_info_button = ttk.Button(self.mainframe, text="Add",
                                           command=self.push_info)
        self.push_info_button.grid(row=3, column=0, sticky="s", columnspan=5)
        self.push_info_button.grid_configure(padx=5, pady=5)
        # Label for price range
        self.price_range_mainlabel = ttk.Label(self.mainframe)
        self.price_range_mainlabel.grid(row=0, column=0, columnspan=2)
        # Hide so that it can't be used until first toplevel is completed
        self.withdraw()

    # function that gets input from the box and does stuff with it
    def push_info(self):
        good = self.good_entry.get()
        self.good_entry.delete(0, "end")
        # Give focus to text box
        self.good_entry.focus_set()
        # If not blank, put data into storage system
        if self.is_blank(good):
            self.makeerror(self.error_label, "This can't be blank")
        else:
            self.store(good)
        # Print all stuff in system for testing purposes
        print()
        for good_ in items:
            print(self.takeaway(good_))

    @staticmethod
    # Not blank function
    def is_blank(input_):
        if input_.isspace() or input_ == "":
            return True
        else:
            return False

    @staticmethod
    # Make an easy storing function
    def store(name):
        name = Item(name)
        items.append(name)

    @staticmethod
    # Getting data from specified object
    def takeaway(item_):
        returner = []
        for att in vars(item_).values():
            returner.append(att)
        return returner


# First top level with price range box and units
class FirstTopLevel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # Configure window
        self.configure(background="#97dbe5")
        self.geometry("400x400")
        # Padding frame
        self.padder = ttk.Frame(self, width=100, height=100, style="PadFrame.TFrame")
        self.padder.grid(row=0, column=0)
        # Main frame
        self.info_frame = ttk.Frame(self, padding=15)
        self.info_frame.grid(row=1, column=1)
        # Error label
        self.price_range_error = ttk.Label(self.info_frame, text="", style="Error.TLabel")
        self.price_range_error.grid(row=0, column=1)
        # Box to enter price range
        self.price_range_box = ttk.Entry(self.info_frame, width=9)
        self.price_range_box.grid(row=1, column=1)
        # Enter key binding
        self.price_range_box.bind("<Return>", lambda event: self.check())
        # Set focus on first widget
        self.price_range_box.focus_set()
        # Label for info
        self.price_range_label = ttk.Label(self.info_frame, text="Price"
                                                                 " range:  $")
        self.price_range_label.grid(row=1, column=0)
        self.check_button = ttk.Button(self.info_frame, text="Ok, go!",
                                       command=lambda: self.check())
        self.check_button.grid(row=2, column=0, columnspan=2)
        self.check_button.grid_configure(padx=20, pady=5)

    def check(self):
        self.price_range_box.focus_set()
        if self.is_blank(self.price_range_box.get()):
            self.makeerror(self.price_range_error, "This can't be blank!")
        elif self.check_int(self.price_range_box.get()):
            self.makeerror(self.price_range_error, "This has to be an integer"
                                                   "!")
        else:
            root.price_range.set(self.price_range_box.get())
            root.deiconify()
            root.good_entry.focus_set()
            root.price_range_mainlabel.configure(
                text=f"Your price range is "
                f"${root.price_range.get():.2f}")
            self.after_cancel(self)
            self.destroy()

    @staticmethod
    # Not blank function
    def is_blank(input_):
        if input_.isspace() or input_ == "":
            return True
        else:
            return False

    @staticmethod
    # Check int function
    def check_int(to_check):
        try:
            # Returns false if the code works, if it doesn't the try kicks in
            int(to_check)
            return False
        except ValueError:
            return True

    # Makes the error message
    def makeerror(self, label, error_message):
        label.configure(text=error_message)
        # Hides the text
        self.after(5000, lambda: label.configure(text=""))


# Make the storage class
class Item:
    def __init__(self, name):
        self.name = name


items = []
root = Root()
first_window = FirstTopLevel(root)
tk.mainloop()
