import tkinter as tk
from functools import partial
from tkinter import ttk
from Code.Examples.Showbox import ShowBox
from Code.Lexicon import Parameter as Para


class Window(ttk.Frame):

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.pack = self.build(self.pack)

        self.left_side = ttk.Frame(self)
        self.right_side = ttk.Frame(self)


        self.check_values = dict(checkvar=[], checkbutton=[])
        for key in Para.media_tabel_identifier.keys():
            var = tk.StringVar()
            cbutton = ttk.Checkbutton(self.left_side, text=key, variable=var, onvalue=key, offvalue=None)
            self.check_values['checkvar'].append(var)
            self.check_values['checkbutton'].append(cbutton)

        self.choice = tk.StringVar()
        values = list(Para.media_search_columns.keys())
        self.options = ttk.OptionMenu(self.right_side, self.choice, values[0], *values)

        self.entry = ttk.Entry(self.right_side)
        self.search = ttk.Button(self.right_side, text='Suche', command=self.search)
        self.showbox = ShowBox(self)


    def search(self):
        term = self.entry.get()
        column = self.choice.get()
        for cb in self.check_values['checkvar']:
            if cb.get():
                 # TODO make sql statement here, cb.get returns mediatype
                print(cb.get(), column, term)# TODO translate to db_talk by Lexicon.py or maybe while instancing
                #call showbox.fill_window inside loop




    def build(self, pack):
        def wrapper(**kwargs):
            pack(kwargs)

            self.showbox.pack(side='bottom')
            self.right_side.pack(side='right')
            self.left_side.pack(side='left')

            for item in self.check_values['checkbutton']:
                item.pack(anchor='w')

            self.options.pack(anchor='e', fill='x', pady=3, padx=1)
            self.entry.pack(anchor='e', fill='x', pady=3, padx=1)
            self.search.pack(anchor='e', fill='x', pady=3)

        return wrapper




if __name__ == '__main__':
    root = tk.Tk()
    label = Window(root)
    label.pack()
    root.mainloop()