import tkinter as tk

class ListWidget(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self._pack = tk.Frame.pack

        self.lab1 = tk.Label(self, text='No1')
        self.lab2 = tk.Label(self, text='No2')
        self.lab3 = tk.Label(self, text='No3')
        self.button = tk.Button(self, text='Bu1', command=self.test)


    def pack(self, **kwargs):
        self._pack(self,**kwargs)
        self.lab1.pack(side='left')
        self.lab2.pack(side='left')
        self.lab3.pack(side='left')
        self.button.pack(side='left')


    def test(self):
        print('some')






if __name__ == '__main__':
    root = tk.Tk()
    text = tk.Text(root, width=100)
    text.pack()
    for i in range(59):
        text.window_create('end',window=ListWidget(root).pack())
    text.window_create('end', window=ListWidget(text).pack())
    text.window_create('end', window=ListWidget(text).pack())
    text.window_create('end', window=ListWidget(text).pack())

    root.mainloop()