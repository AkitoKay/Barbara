import tkinter as tk
import tkinter.ttk as ttk
from Examples.Showbox import ShowBox

class details(tk.Toplevel):

    def __init__(self, root):
        super().__init__(root)
        self.geometry('400x300')
        self.title('Details')


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x300')
        self.title('Main Window')

    def open_window(self):
        window = details(self)
        window.grab_set()


if __name__ == "__main__":
    app = App()
    """one_data = ('1',
                'Harry Potter and the Half-Blood Prince (Harry Potter  #6)',
                'J.K. Rowling-Mary GrandPré',
                'Harding Alvin W.',
                '2011-10-23',
                '1')"""

    more_data = [('1', 'Test Book 1', 'Test Author 1', 'Test Publisher 1', 'Release 1', '1'),
                 ('2', 'Test Book 2', 'Test Author 2', 'Test Publisher 2', 'Release 2', '2'),
                 ('3', 'Test Book 3', 'Test Author 3', 'Test Publisher 3', 'Release 3', '3'),
                 ('4', 'Test Book 4', 'Test Author 4', 'Test Publisher 4', 'Release 4', '4'),
                 ('5', 'Test Book 5', 'Test Author 5', 'Test Publisher 5', 'Release 5', '5'),
                 ('6', 'Test Book 6', 'Test Author 6', 'Test Publisher 6', 'Release 6', '6'),
                 ]
    """for i in range(15):
        more_data.append(one_data)"""

    t = lambda: s.fill_window(more_data)

    s = ShowBox(app)
    t = lambda: s.fill_window(more_data)

    s.pack(side='left')
    t()

    app.mainloop()