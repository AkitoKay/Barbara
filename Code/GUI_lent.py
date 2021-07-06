import tkinter as tk
import tkinter.ttk as ttk
from Barbara.Code.Examples.Showbox import ShowBox

class Window(ttk.Frame):
    def __init__(self, root, **kwargs):
        ttk.Frame.__init__(self, root, **kwargs)
        self._pack = ttk.Frame.pack


        self.check_values = []
        for i in range(3):
           self.check_values.append(tk.BooleanVar(root, False))


        #instance your objects here
        self.left_side = ttk.Frame(self)
        self.right_side = ttk.Frame(self)
        
        self.showbox = ShowBox(self)
        self.buttonLent = ttk.Button(self.right_side, text='Lent', width=20)
        self.buttonOverdue = ttk.Button(self.right_side, text='Overdue', width=20)
        self.checkbuttonMovie = ttk.Checkbutton(self.left_side, text='Movies', var=self.check_values[0])
        self.checkbuttonMusic = ttk.Checkbutton(self.left_side, text='Music', var=self.check_values[1])
        self.checkbuttonLiterature = ttk.Checkbutton(self.left_side, text='Literature', var=self.check_values[2])
        
    def pack(self, **kwargs):
        #call .pack() for instanced objects here
        self._pack(self, **kwargs)
        self.showbox.pack(side='bottom')

        self.left_side.pack(side='left')
        self.right_side.pack(side='right')

        self.buttonLent.pack(pady=5, padx=40, side='top', anchor='w')
        self.buttonOverdue.pack(pady=5, padx=40, side='top', anchor='w')
        self.checkbuttonMusic.pack(anchor='w')
        self.checkbuttonMovie.pack(anchor='w')
        self.checkbuttonLiterature.pack(anchor='w')






        
if __name__=='__main__':
    root = tk.Tk()
    root.geometry()
    s = Window(root)
    s.pack()
    root.mainloop()

#test
