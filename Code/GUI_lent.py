import tkinter as tk
from tkinter import ttk


class Window(ttk.Frame):

    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        self._pack = ttk.Frame.pack

        #instance your objects here
        self.label = ttk.Label(self, text='Insert code for lent page here')        



        
    def pack(self, **kwargs):
        #call .pack() for instanced objects here
        self._pack(self, kwargs)
        self.label.pack()


        
if __name__=='__main__':
    root = tk.Tk()
    label = Window(root)
    label.pack()
    root.mainloop()
