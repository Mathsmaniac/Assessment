"""
Added Scrolling_Listv2.py
"""
import tkinter as tk
from tkinter import ttk


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        # Declare style
        s = ttk.Style()
        s.configure("TFrame", background="#02fa82")
        s.configure("PadFrame.TFrame", borderwidth=0, relief="",
                    background="#97dbe5")
        s.configure("Error.TLabel", foreground="red")
        s.configure("MainFrame.TFrame", borderwidth=5, relief="ridge")
        s.configure("TLabel", background="#02fa82")
        s.configure("TMenubutton", background="#009947")
        s.configure("BigLabel.TLabel", font=("Ariel", 10))
        # Options for drop down list
        self.options = ["mg", "g", "kg", "st", "oz", "lb", "t", "mL", "L"]
        # Variable for price range
        self.price_range = tk.IntVar()
        # Variable for item selected for drop down list
        self.selected = tk.StringVar()
        # Configure window
        self.title("Price Compare Tool")
        self.geometry("700x600")
        self.configure(background="#97dbe5")
        # Padding frame
        self.pad_frame = ttk.Frame(self, width=150, height=150,
                                   style="PadFrame.TFrame")
        self.pad_frame.grid(row=0, column=0)
        # Main frame
        self.mainframe = ttk.Frame(self, padding="15",
                                   style="MainFrame.TFrame")
        self.mainframe.grid(row=1, column=1, sticky=("n", "w", "e", "s"))
        # Error label for good box
        self.error_label = ttk.Label(self.mainframe, style="Error.TLabel")
        self.error_label.grid(row=2, column=2, sticky=("s", "w"), columnspan=2)
        # Entry box for good name
        self.good_entry = ttk.Entry(self.mainframe, width=20)
        self.good_entry.grid(row=3, column=2, sticky="n")
        # Info label
        self.good_entry_info = ttk.Label(self.mainframe, text="Item name: ")
        self.good_entry_info.grid(row=3, column=1, sticky="n")
        # Drop down list widget
        self.drop = ttk.OptionMenu(self.mainframe, self.selected,
                                   self.options[1], *self.options,
                                   command=lambda event: self.drop_update())
        self.drop.grid(row=1, column=2, sticky="W", pady=(10, 0))
        # Drop down list info
        self.drop_info = ttk.Label(self.mainframe, text="Unit: ")
        self.drop_info.grid(row=1, column=1, sticky=("E", "S", "N"))
        # Button to store info
        self.push_info_button = ttk.Button(self.mainframe, text="Add",
                                           command=self.push_info)
        self.push_info_button.grid(row=5, column=1, sticky="s", columnspan=5)
        self.push_info_button.grid_configure(padx=5, pady=15)
        # Label for price range
        self.price_range_mainlabel = ttk.Label(self.mainframe,
                                               style="BigLabel.TLabel")
        self.price_range_mainlabel.grid(row=0, column=0, columnspan=5)
        # Frame for all amount of units widgets
        self.amount_of_units_frame = ttk.Frame(self.mainframe)
        self.amount_of_units_frame.grid(row=4, column=1, columnspan=3,
                                        sticky="w")
        # Box for amount of units
        self.amount_of_units_box = ttk.Entry(self.amount_of_units_frame,
                                             width=7)
        self.amount_of_units_box.grid(row=1, column=1, sticky=("w", "e"))
        # Error label for amount of units
        self.amount_of_units_error = ttk.Label(self.amount_of_units_frame,
                                               style="Error.TLabel")
        self.amount_of_units_error.grid(row=0, column=1, sticky="w",
                                        columnspan=3)
        # Info label for amount of units
        self.amount_of_units_info = ttk.Label(self.amount_of_units_frame,
                                              text="Amount: ")
        self.amount_of_units_info.grid(row=1, column=0, sticky="e")
        # Other label showing unit type
        self.unit_type_info = ttk.Label(self.amount_of_units_frame,
                                        text=self.selected.get())
        self.unit_type_info.grid(row=1, column=2, sticky="w")
        # Listbox component
        self.listbox = tk.Listbox(self.mainframe, width=30)
        self.listbox.grid(row=1, column=0, rowspan=4, padx=10, pady=10)
        # Scrollbar for the listbox
        self.scroller = ttk.Scrollbar(self.mainframe)
        self.scroller.grid(row=1, column=0, sticky="n, e, s", rowspan=4,
                           padx=10, pady=10)
        # Set up scrolling function
        self.listbox.config(yscrollcommand=self.scroller.set)
        self.scroller.config(command=self.listbox.yview)
        # Button to delete items from listbox
        self.item_delete_button = ttk.Button(self.mainframe, text="Delete",
                                             command=lambda:
                                             self.delete_selected())
        self.item_delete_button.grid(row=5, column=0)
        # Enter key bindings
        self.good_entry.bind("<Return>",
                             lambda event: self.amount_of_units_box.focus_set()
                             )
        self.amount_of_units_box.bind("<Return>",
                                      lambda event: self.push_info())
        # Hide so that it can't be used until first toplevel is completed
        self.withdraw()

    # function that gets input from the box and does stuff with it
    def push_info(self):
        good = self.good_entry.get()
        units = self.amount_of_units_box.get()
        # If not blank, put data into storage system
        if self.is_blank(good):
            self.makeerror(self.error_label, "This can't be blank")
            # Give focus to item text box
            self.good_entry.focus_set()
            # Check if other box is non-int or blank aswell
            # so that all relevant errors can be addressed
            if self.is_blank(units):
                self.makeerror(self.amount_of_units_error,
                               "This can't be blank!")
            elif self.check_int(units):
                self.makeerror(self.amount_of_units_error,
                               "This has to be an integer")
        elif self.is_blank(units):
            self.makeerror(self.amount_of_units_error, "This can't be blank")
            # Give focus to amount of units text box
            self.amount_of_units_box.focus_set()
        elif self.check_int(units):
            self.makeerror(self.amount_of_units_error,
                           "This has to be an integer")
            # Give focus to amount of units text box
            self.amount_of_units_box.focus_set()
        else:
            self.good_entry.delete(0, "end")
            self.amount_of_units_box.delete(0, "end")
            self.store(good, units)
            self.go_listbox()
            self.good_entry.focus_set()

    def drop_update(self):
        self.unit_type_info.configure(text=self.selected.get())
        self.go_listbox()

    # Add items to the listbox
    def go_listbox(self):
        self.listbox.delete(0, "end")
        for item in items:
            self.listbox.insert('end', f"{self.takeaway(item)[1]}"
                                       f"{self.selected.get()} of "
                                       f"{self.takeaway(item)[0]}")

    # Delete items from the textbox
    def delete_selected(self):
        # Delete selected items from the actual list
        for i in self.listbox.curselection():
            items.pop(i)
        # Remake the list
        self.go_listbox()

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

    @staticmethod
    # Make an easy storing function
    def store(name, amount):
        name = Item(name, amount)
        items.append(name)

    @staticmethod
    # Getting data from specified object
    def takeaway(item_):
        returner = []
        for att in vars(item_).values():
            returner.append(att)
        return returner

    # Makes the error message
    def makeerror(self, label, error_message):
        label.configure(text=error_message)
        # Hides the text
        self.after(5000, lambda: label.configure(text=""))


# First top level with price range box and units
class FirstTopLevel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # Declare variables
        self.options = ["Unit:", "mg", "g", "kg", "t", "st", "oz", "lb",
                        "mL", "L"]
        # Configure window
        self.configure(background="#97dbe5")
        self.geometry("400x400")
        # Padding frame
        self.padder = ttk.Frame(self, width=100, height=100,
                                style="PadFrame.TFrame")
        self.padder.grid(row=0, column=0)
        # Main frame
        self.info_frame = ttk.Frame(self, padding=15)
        self.info_frame.grid(row=1, column=1)
        # Error label for price range box
        self.price_range_error = ttk.Label(self.info_frame, text="",
                                           style="Error.TLabel")
        self.price_range_error.grid(row=0, column=1)
        # Error label for drop down list
        self.unit_error = ttk.Label(self.info_frame, text="",
                                    style="Error.TLabel")
        self.unit_error.grid(row=0, column=2)
        # Box to enter price range
        self.price_range_box = ttk.Entry(self.info_frame, width=9)
        self.price_range_box.grid(row=1, column=1, sticky="W")
        # Enter key binding
        self.price_range_box.bind("<Return>", lambda event: self.check())
        # Set focus on first widget
        self.price_range_box.focus_set()
        # Label for info
        self.price_range_label = ttk.Label(self.info_frame, text="Price"
                                                                 " range:  $")
        self.price_range_label.grid(row=1, column=0)
        # Button to submit
        self.check_button = ttk.Button(self.info_frame, text="Ok, go!",
                                       command=lambda: self.check())
        self.check_button.grid(row=2, column=0, columnspan=6)
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
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


if __name__ == "__main__":
    items = []
    root = Root()
    first_window = FirstTopLevel(root)
    tk.mainloop()
