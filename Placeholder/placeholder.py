from tkinter import *
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme="equilux")
root.title("PlaceHolder Tutorial")

style = ttk.Style(root)

testframe = ttk.Frame(root)
testframe.grid(row = 0, column = 0, sticky = "news")

class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder,validation, *args, **kwargs):
        super().__init__(container, *args, style="Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder
        self.validation = validation

        self.insert("0", self.placeholder)
        self.configure(validate="key", validatecommand=(charactervalidation, "%P"))
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder,)


    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self.addvalidation()
            self["style"] = "TEntry"

    def _add_placeholder(self, e):
        if not self.get():
            self.removevalidation()
            self.insert("0", self.placeholder)
            self["style"] = "Placeholder.TEntry"

    def removevalidation(self):
        if self.validation == "character":
            self.configure(validate = "none", validatecommand = (charactervalidation, "%P"))
        if self.validation == "none":
            self.configure(validate="none", validatecommand=(charactervalidation, "%P"))
        if self.validation == "time":
            self.configure(validate="none", validatecommand=(timevalidation, "%P"))
        if self.validation == "number":
            self.configure(validate="none", validatecommand=(numbervalidation, "%P"))

    def addvalidation(self):
        if self.validation == "character":
            self.configure(validate = "key", validatecommand = (charactervalidation, "%P"))
        if self.validation == "none":
            self.configure(validate="none", validatecommand=(charactervalidation, "%P"))
        if self.validation == "number":
            self.configure(validate="key", validatecommand=(numbervalidation, "%P"))
        if self.validation == "time":
            self.configure(validate="key", validatecommand=(timevalidation, "%P"))
    #         Key validate whenever any keystroke changes the widget's contents

    def addcensorship(self):
        if self.validation == "password":
            show = "*"

def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def only_character_input(P):
    if P.isalpha() or P == "":
        return True
    return False

def only_time_input(P):
    text = P  # e.get()

    parts = text.split(':')
    parts_number = len(parts)

    if parts_number > 2:
        return False

    if parts_number > 1 and parts[1]:
        if not parts[1].isdecimal() or len(parts[1]) > 2:
            return False

    if parts_number > 0 and parts[0]:  # don't check empty string
        if not parts[0].isdecimal() or len(parts[0]) > 8:
            # print('wrong first part')
            return False

    return True


# Register is to check every keystroke the character enters
# Then checks if the keystroke is valid for that specific function
charactervalidation = root.register(only_character_input)
numbervalidation = root.register(only_numeric_input)
timevalidation = root.register(only_time_input)

numberPlaceHolder= PlaceholderEntry(testframe,"Number", "number")
numberPlaceHolder.grid(row = 1, column = 1, columnspan = 3,pady = 10)
timePlaceHolder = PlaceholderEntry(testframe,"Time","time")
timePlaceHolder.grid(row = 2, column = 1, padx = 100,pady = 10)
charPlaceHolder = PlaceholderEntry(testframe,"Character","character")
charPlaceHolder.grid(row = 3, column = 1,pady = 10)

mainloop()