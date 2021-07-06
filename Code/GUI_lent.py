import tkinter as tk
import tkinter.ttk as ttk
from Barbara.Code.Examples.Showbox import ShowBox
from Barbara.Code.db_connector import DB

class Window(ttk.Frame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.pack = self.build(self.pack)

        self.check_values = []
        for i in range(3):
           self.check_values.append(tk.BooleanVar(root, False))

        #instance your objects here
        self.left_side = ttk.Frame(self)
        self.right_side = ttk.Frame(self)
        
        self.showbox = ShowBox(self)
        self.buttonLent = ttk.Button(self.right_side, text='Lent', command=self.get_lent ,width=20)
        self.buttonOverdue = ttk.Button(self.right_side, text='Overdue',command=self.get_overdue, width=20)
        self.checkbuttonMovie = ttk.Checkbutton(self.left_side, text='Movies', var=self.check_values[0])
        self.checkbuttonMusic = ttk.Checkbutton(self.left_side, text='Music', var=self.check_values[1])
        self.checkbuttonLiterature = ttk.Checkbutton(self.left_side, text='Literature', var=self.check_values[2])


    def build(self, pack):
        def wrapper(**kwargs):
            pack(kwargs)
            self.showbox.pack(side='bottom')

            self.left_side.pack(side='left')
            self.right_side.pack(side='right')

            self.buttonLent.pack(pady=5, padx=40, side='top', anchor='w')
            self.buttonOverdue.pack(pady=5, padx=40, side='top', anchor='w')
            self.checkbuttonMusic.pack(anchor='w')
            self.checkbuttonMovie.pack(anchor='w')
            self.checkbuttonLiterature.pack(anchor='w')
        return wrapper

    def get_overdue(self):
        index = 0
        dataset = []
        for cb in self.check_values:
            #0=movies, 1=music , 2=liter
            if cb.get():
                if index == 0:
                    # TODO send request
                    # select * From 'Ausgeliehen' where aktuelles Datum > Ausleihdatum + x
                    # Join 'Bücher' ON 'id'
                    #dataset.append(Ergebnis)
                    dataset = DB.get_tes()
                if index == 1:
                    #TODO send request
                    pass
                if index == 2:
                    # TODO send request
                    pass

                self.showbox.fill_window(dataset)
            index+=1

    def get_lent(self):
        dataset = []
        index = 0
        for cb in self.check_values:
            # 0=movies, 1=music , 2=liter
            if cb.get():
                if index == 0:
                    # TODO send request
                    # select * From 'Ausgeliehen' where Auslehdatum = None
                    # Join 'Bücher' ON 'id'
                    pass
                if index == 1:
                    # TODO send request
                    pass
                if index == 2:
                    # TODO send request
                    pass
            index += 1





if __name__=='__main__':
    root = tk.Tk()
    root.geometry()
    s = Window(root)
    s.pack()
    root.mainloop()

#test
