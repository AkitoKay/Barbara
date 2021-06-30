import tkinter as tk

class ShowBox(tk.Frame):
    def __init__(self, root=None, **kwargs):
        tk.Frame.__init__(self, root, kwargs)
        self.pack = self.build(self.pack)
        #self._pack = tk.Frame.pack
        #self._pack = self.pack
        self.box = tk.Text(self)
        self.ybar = tk.Scrollbar(self)
        self.box.config(yscrollcommand=self.ybar.set)
        self.ybar.config(command=self.box.yview)
        
    def build(self, pack):
        def wrapper(**kwargs):
            pack(kwargs)
            self.box.pack(side='left')
            self.ybar.pack(side='right',fill='y')
        return wrapper

if __name__ == '__main__':
    s = ShowBox()
    s.pack(padx=13)
    
