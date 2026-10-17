from tkinter import *
from tkinter import ttk

class timeConfigClass(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("300x200")
        self.title("Enter a date")

        ttk.Label(self, text="Enter date").pack(pady=20) 