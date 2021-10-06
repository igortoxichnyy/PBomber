#from tkinter import *

import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text="Привет, Tkinter!",
    fg="white",
    bg="black",
    width=20,
    height=20
).pack()

window.mainloop()