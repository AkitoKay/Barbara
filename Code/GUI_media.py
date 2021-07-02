import tkinter as tk
from functools import partial
from tkinter import ttk


class Window(ttk.Frame):

    def __init__(self, root, **kwargs):
        ttk.Frame.__init__(self, root, **kwargs)
        self._pack = ttk.Frame.pack

        #instance your objects here
        #self.label = ttk.Label(self, text='Insert code for media page here')
        self.style = ttk.Style().configure('Frame1.TFrame', background='red')   #Frame Debug Tool
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.cbvar = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
        self.topframe1 = ttk.Frame(self)
        self.topframe2 = ttk.Frame(self)
        self.centerframe1 = ttk.Frame(self, style='Frame1.TFrame')
        self.checkbox1 = ttk.Checkbutton(self.topframe1,
                                         text='Music', variable=self.cbvar[0], onvalue='music', offvalue='')
        self.checkbox2 = ttk.Checkbutton(self.topframe1,
                                         text='Movie', variable=self.cbvar[1], onvalue='movie', offvalue='')
        self.checkbox3 = ttk.Checkbutton(self.topframe1,
                                         text='Literature', variable=self.cbvar[2], onvalue='literature', offvalue='')
        self.checkbox4 = ttk.Checkbutton(self.topframe1,
                                         text='Misc', variable=self.cbvar[3], onvalue='misc', offvalue='')
        self.dropdown = ttk.Combobox(self.topframe2,
                                     values=('Author', 'Title', 'Publisher', 'Year', 'Location'), state='readonly')
        self.entry = ttk.Entry(self.topframe2)
        self.search = ttk.Button(self.topframe2, text='Search')
        self.showbox = tk.Label(self.centerframe1, text='Hier könnte ihre Showbox stehen!', height=29)
        self.debugg = ttk.Button(self.centerframe1, text='test', command=self.debugger)

    def pack(self, **kwargs):

        #call .pack() for instanced objects here
        self._pack(self, **kwargs)
        self.topframe1.grid(row=0, column=0, sticky='NESW')
        self.topframe2.grid(row=0, column=1, sticky='NESW')
        self.centerframe1.grid(row=1, column=0, columnspan=2, sticky='NESW')
        self.checkbox1.pack(side='top', anchor='w', padx=10)
        self.checkbox2.pack(side='top', anchor='w', padx=10)
        self.checkbox3.pack(side='top', anchor='w', padx=10)
        self.checkbox4.pack(side='top', anchor='w', padx=10)
        self.dropdown.pack(side='top', anchor='e', fill='x', padx=10, pady=2)
        self.entry.pack(side='top', anchor='e', fill='x', padx=10, pady=2)
        self.search.pack(side='top', anchor='e', fill='x', padx=10, pady=2)
        self.showbox.pack(side='top', anchor='center', fill='both', padx = 10, pady=10)
        self.debugg.pack(side='bottom')

    def debugger(self):
        print(self.cbvar[0].get(), self.cbvar[1].get(), self.cbvar[2].get(), self.cbvar[3].get())
        #print(self.entry1.get(), self.entry2.get(), self.entry3.get())



if __name__ == '__main__':

    root = tk.Tk()
    label = Window(root)
    label.pack()
    root.mainloop()
