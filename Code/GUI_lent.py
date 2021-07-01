import tkinter as tk
import tkinter.ttk as ttk
from functools import partial
from TextBox import ShowBox

class Window(ttk.Frame):
    def __init__(self, root, **kwargs):
        ttk.Frame.__init__(self, root, **kwargs)
        self._pack = ttk.Frame.pack

        self.chkValue1 = tk.BooleanVar()
        self.chkValue1.set(False)

        self.chkValue2 = tk.BooleanVar()
        self.chkValue2.set(False)

        self.chkValue3 = tk.BooleanVar()
        self.chkValue3.set(False)

        self.chkValue4 = tk.BooleanVar()
        self.chkValue4.set(False)

        self.chkValue5 = tk.BooleanVar()
        self.chkValue5.set(False)


        #instance your objects here
        self.label = ttk.Label(self, text='Insert code for lent page here')

        self.showbox = ShowBox(self, command=None)
        self.buttonLent = ttk.Button(self, text='Lent', width=20)
        self.buttonOverdue = ttk.Button(self, text='Overdue', width=20)
        self.checkbuttonMovie = ttk.Checkbutton(self, text='Movies', var=self.chkValue1)
        self.checkbuttonMusic = ttk.Checkbutton(self, text='Music', var=self.chkValue2)
        self.checkbuttonLiterature = ttk.Checkbutton(self, text='Literature', var=self.chkValue3)
        self.checkbuttonOthers = ttk.Checkbutton(self, text='Others', var=self.chkValue4)
        self.checkbuttonAll = ttk.Checkbutton(self, text='All', var=self.chkValue5)

    def pack(self, **kwargs):
        #call .pack() for instanced objects here
        self._pack(self, **kwargs)
        self.label.pack(side='top')
        self.showbox.pack(side='bottom')

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
