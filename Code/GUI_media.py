import tkinter as tk
from functools import partial
from tkinter import ttk


class Window(ttk.Frame):

    def __init__(self, root, **kwargs):
        ttk.Frame.__init__(self, root, **kwargs)
        self._pack = ttk.Frame.pack

        #instance your objects here
        #self.label = ttk.Label(self, text='Insert code for media page here')
        self.cbvar = [tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()]
        self.topframe1 = ttk.Frame(self)
        self.topframe2 = ttk.Frame(self)
        self.centerframe1 = ttk.Frame(self)
        self.checkbox1 = ttk.Checkbutton(self.topframe1, text='music', variable=self.cbvar[0])
        self.checkbox2 = ttk.Checkbutton(self.topframe1, text='movie', variable=self.cbvar[1])
        self.checkbox3 = ttk.Checkbutton(self.topframe1, text='literature', variable=self.cbvar[2])
        self.checkbox4 = ttk.Checkbutton(self.topframe1, text='misc', variable=self.cbvar[3])
        self.entry1 = ttk.Entry(self.topframe2)
        self.entry2 = ttk.Entry(self.topframe2)
        self.entry3 = ttk.Entry(self.topframe2)
        self.debugg = ttk.Button(self, text='test', command=self.debugger)

    def pack(self, **kwargs):

        #call .pack() for instanced objects here
        self._pack(self, **kwargs)
        #self.label.pack(side ='bottom')
        self.topframe1.pack(side='left', fill='both', pady = 10)
        self.topframe2.pack(side='right', fill='both', pady = 10)
        self.checkbox1.pack(side='top', anchor='w', padx=10)
        self.checkbox2.pack(side='top', anchor='w', padx=10)
        self.checkbox3.pack(side='top', anchor='w', padx=10)
        self.checkbox4.pack(side='top', anchor='w', padx=10)
        self.entry1.pack(side='top', anchor='e', fill='x', padx=10, pady=2)
        self.entry2.pack(side='top', anchor='e', fill='x', padx=10, pady=2)
        self.entry3.pack(side='top', anchor='e', fill='x', padx=10, pady=2)
        self.debugg.pack(side='bottom')

    def debugger(self):
        #print(self.cbvar[0].get(), self.cbvar[1].get(), self.cbvar[2].get(), self.cbvar[3].get())
        print(self.entry1.get(), self.entry2.get(), self.entry3.get())



if __name__ == '__main__':

    root = tk.Tk()
    label = Window(root)
    label.pack()
    root.mainloop()
