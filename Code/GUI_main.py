import tkinter as tk                    
from tkinter import ttk

from GUI_lent import Window as Lent
from GUI_media import Window as Media

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Barbara")
        self.geometry('800x650')
        self.resizable(False, False)

        self.tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
  
        self.tabControl.add(self.tab1, text ='lent')
        self.tabControl.add(self.tab2, text ='media')
        self.tabControl.pack(expand = 1, fill ="both")

        self.lent = Lent(self.tab1)
        self.media = Media(self.tab2)

        self.lent.pack(expand='true', fill='both')
        self.media.pack()
        
  
if __name__=='__main__':
    barbara = App()
    barbara.mainloop()
