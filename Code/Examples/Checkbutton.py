import tkinter as tk
from tkinter import ttk

root = tk.Tk()
var = tk.IntVar()

def test():
    print(var.get())

cb = ttk.Checkbutton(root, text='test', variable=var).pack()
b1 = tk.Button(root, text='print', command=test).pack()

root.mainloop()