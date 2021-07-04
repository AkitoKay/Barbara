import tkinter as tk
from tkinter import ttk
from Code.Showbox import ShowBox

class Window(ttk.Frame):
    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        self._pack = ttk.Frame.pack

        #instance your objects here
        self.label = ttk.Label(self, text='Insert code for media page here', theme='black')
        s = ShowBox(self).pack()


        
    def pack(self, **kwargs):
        #call .pack() for instanced objects here
        self._pack(self, kwargs)
        self.label.pack()


        
if __name__=='__main__':
    root = tk.Tk()
    label = Window(root)
    label.pack()
    root.mainloop()
