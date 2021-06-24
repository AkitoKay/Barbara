import tkinter as tk

class MyWidget(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self._pack = tk.Frame.pack
        self.l1 =tk.Label(self, text='Label1', bg='blue')
        self.l2 =tk.Label(self, text='Label2', bg='red')

    
    def pack(self, **kwargs):
        self._pack(self, kwargs)
        self.l1.pack(fill='x')
        self.l2.pack(fill='x')


if __name__=='__main__':
    root = tk.Tk()
    root.geometry('500x200')
    mw = MyWidget(root)
    mw.pack()#fill='x')
    root.mainloop()
