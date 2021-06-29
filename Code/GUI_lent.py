import tkinter as tk
import tkinter.ttk as ttk
from functools import partial

class Window(ttk.Frame):
    def __init__(self, root, **kwargs):
        ttk.Frame.__init__(self, root, **kwargs)
        self._pack = ttk.Frame.pack

        #instance your objects here
        self.label = ttk.Label(self, text='Insert code for lent page here')

        self.listbox = tk.Listbox(self, command=None, width=800, height=28)
        self.buttonLent = ttk.Button(self, text='Lent', width=20)
        self.buttonOverdue = ttk.Button(self, text='Overdue', width=20)
        self.checkbuttonMovie = ttk.Checkbutton(self, text='Movies')
        self.checkbuttonMusic = ttk.Checkbutton(self, text='Music')
        self.checkbuttonLiterature = ttk.Checkbutton(self, text='Literature')
        self.checkbuttonOthers = ttk.Checkbutton(self, text='Others')
        self.checkbuttonAll = ttk.Checkbutton(self, text='All')

    def pack(self, **kwargs):
        #call .pack() for instanced objects here
        self._pack(self, **kwargs)
        self.label.pack(side='top')
        self.listbox.pack(side='bottom')

        self.buttonLent.pack(pady=5, padx=40, side='top', anchor='w')
        self.buttonOverdue.pack(pady=5, padx=40, side='top', anchor='w')
        self.checkbuttonMusic.pack(side='right', anchor='n')
        self.checkbuttonMovie.pack(side='right', anchor='n')
        self.checkbuttonLiterature.pack(side='right', anchor='n')
        self.checkbuttonOthers.pack(side='right', anchor='n')
        self.checkbuttonAll.pack(side='right', anchor='n')

        
if __name__=='__main__':
    root = tk.Tk()
    root.geometry('800x600')
    frame = Window(root)
    frame.pack(expand='true', fill='both')
    root.mainloop()
