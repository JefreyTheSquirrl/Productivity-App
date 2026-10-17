from tkinter import *
from tkinter import ttk
import newEvent

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def open_time_config():
    newEvent.timeConfigClass(root)

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Create Event", command=open_time_config).grid(column=1, row=0)
root.title("Productivity App")

root.mainloop()