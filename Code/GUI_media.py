import tkinter as tk
from functools import partial
from tkinter import ttk
#<<<<<<< Updated upstream
import Showbox as Sb
import mysql.connector
#=======
from Examples.Showbox import ShowBox
from Lexicon import Parameter as Para
#>>>>>>> Stashed changes


class Window(ttk.Frame):

    def __init__(self, root, **kwargs):
        ttk.Frame.__init__(self, root, **kwargs)
        self._pack = ttk.Frame.pack

        #instance your objects here
        #self.label = ttk.Label(self, text='Insert code for media page here')
        #self.style = ttk.Style().configure('Frame1.TFrame', background='red')   #Frame Debug Tool
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.cbvar = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
        self.topframe1 = ttk.Frame(self, padding=5)
        self.topframe2 = ttk.Frame(self, padding=5)
        self.centerframe1 = ttk.Frame(self, padding=5)
        self.checkbox1 = ttk.Checkbutton(self.topframe1,
                                         text='Music', variable=self.cbvar[0], onvalue='music', offvalue='')
        self.checkbox2 = ttk.Checkbutton(self.topframe1,
                                         text='Movie', variable=self.cbvar[1], onvalue='movie', offvalue='')
        self.checkbox3 = ttk.Checkbutton(self.topframe1,
                                         text='Literature', variable=self.cbvar[2], onvalue='literature', offvalue='')
        self.checkbox4 = ttk.Checkbutton(self.topframe1,
                                         text='Misc', variable=self.cbvar[3], onvalue='misc', offvalue='')
        self.dropdown = ttk.Combobox(self.topframe2,
                                     values=('Author', 'Title', 'Publisher', 'Year', 'Location'), state='readonly')
        self.entry = ttk.Entry(self.topframe2)
        self.search = ttk.Button(self.topframe2, text='Search',
                                 command=lambda:self.showbox.fill_window(self.get_data(self.cbvar)))
        #self.showbox = tk.Label(self.centerframe1, text='Hier könnte ihre Showbox stehen!', height=28)
        self.showbox = Sb.ShowBox(self.centerframe1)
        #self.debugg = ttk.Button(self.centerframe1, text='test', command=self.debugger)

    def pack(self, **kwargs):

        #call .pack() for instanced objects here
        self._pack(self, **kwargs)
        self.topframe1.grid(row=0, column=0, sticky='NESW', padx=60, pady=5)
        self.topframe2.grid(row=0, column=1, sticky='NESW', padx=57, pady=5)
        self.centerframe1.grid(row=1, column=0, columnspan=2, sticky='NESW')
        self.checkbox1.pack(side='top', anchor='w')
        self.checkbox2.pack(side='top', anchor='w')
        self.checkbox3.pack(side='top', anchor='w')
        self.checkbox4.pack(side='top', anchor='w')
        self.dropdown.pack(side='top', anchor='e', fill='x', pady=3, padx=5)
        self.entry.pack(side='top', anchor='e', fill='x', pady=3, padx=5)
        self.search.pack(side='top', anchor='e', fill='x', pady=3, padx=5)
        self.showbox.pack(side='top', anchor='center', pady=5)
        #self.debugg.pack(side='bottom')

    def debugger(self):
        for i in self.cbvar:
            if i.get() != '':
                print(i.get())
        #print(self.entry1.get(), self.entry2.get(), self.entry3.get())

        """def get_data(self, typo):
        db = mysql.connector.connect(user='barbara', password='', host='192.168.8.154', database='barbara')
        cursor = db.cursor()
        query = ('SELECT id, titel, author, publisher, published FROM literature WHERE titel LIKE %s ORDER BY published')
        table = (typo[0].get(), typo[1].get(), typo[2].get(), typo[3].get())
        print(table)
        cursor.execute(query, ('Harry%',))
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result"""



if __name__ == '__main__':

    root = tk.Tk()
    label = Window(root)
    label.pack()
    root.mainloop()
