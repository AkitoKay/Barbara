import tkinter as tk
from functools import partial
from tkinter import ttk
from Barbara.Code.Examples.Showbox import ShowBox


class Window(ttk.Frame):

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.pack = self.build(self.pack)

        self.check_values = []
        for i in range(3):
            self.check_values.append(tk.BooleanVar())

        self.choice = tk.StringVar()

        self.left_side = ttk.Frame(self)
        self.right_side = ttk.Frame(self)



        self.cb_music = ttk.Checkbutton(self.left_side,
                                         text='Music', variable=self.check_values[0])
        self.cb_movie = ttk.Checkbutton(self.left_side,
                                         text='Movie', variable=self.check_values[1])
        self.cb_literature = ttk.Checkbutton(self.left_side,
                                        text='Literature', variable=self.check_values[2])
        values = ('Author', 'Title', 'Publisher', 'Year', 'Location')
        self.options = ttk.OptionMenu(self.right_side, self.choice, values[0], *values
                                      )

        self.entry = ttk.Entry(self.right_side)
        self.search = ttk.Button(self.right_side, text='Search')
        self.showbox = ShowBox(self)


    def build(self, pack):
        def wrapper(**kwargs):
            pack(kwargs)

            self.showbox.pack(side='bottom')
            self.right_side.pack(side='right')
            self.left_side.pack(side='left')

            self.cb_music.pack(anchor='w')
            self.cb_literature.pack(anchor='w')
            self.cb_movie.pack(anchor='w')

            self.options.pack(anchor='e', fill='x', pady=3, padx=1)
            self.entry.pack(anchor='e', fill='x', pady=3, padx=1)
            self.search.pack(anchor='e', fill='x', pady=3)

        return wrapper




if __name__ == '__main__':
    root = tk.Tk()
    label = Window(root)
    label.pack()
    root.mainloop()