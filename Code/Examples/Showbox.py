import tkinter as tk


# id, titel, artist, publisher, release, palcementId
class ListItem(tk.Frame):
    def __init__(self, root=None):
        tk.Frame.__init__(self, root)
        self.pack = self.build(self.pack)

        self.left_side = tk.Frame(self)
        self.right_side = tk.Frame(self)

        # Identifier labels
        self.labl_titel = tk.Label(self.left_side, text='Titel:', anchor='w')
        self.labl_artist = tk.Label(self.left_side, text='Artist:', anchor='w')
        self.labl_publisher = tk.Label(self.left_side, text='Publisher:', anchor='w')
        self.labl_release = tk.Label(self.left_side, text='Release date:', anchor='w')

        # Specific data labels
        self.data_titel = tk.Label(self.right_side, text='some', anchor='w', width=59)
        self.data_artist = tk.Label(self.right_side, text='text', anchor='w', width=59)
        self.data_publisher = tk.Label(self.right_side, text='for', anchor='w', width=59)
        self.data_release = tk.Label(self.right_side, text='instance', anchor='w', width=59)

    def build(self, pack):
        def wrapper(**kwargs):
            pack(kwargs)

            self.left_side.pack(side='left', fill='x')
            self.labl_titel.pack(fill='x')
            self.labl_artist.pack(fill='x')
            self.labl_publisher.pack(fill='x')
            self.labl_release.pack(fill='x')

            self.right_side.pack(side='right')
            self.data_titel.pack(fill='x')
            self.data_artist.pack(fill='x')
            self.data_publisher.pack(fill='x')
            self.data_release.pack(fill='x')

        return wrapper


class ShowBox(tk.Frame):
    def __init__(self, root, **kwargs):
        tk.Frame.__init__(self, root, kwargs)
        self.pack = self.build(self.pack)

        self.box = tk.Canvas(self)
        self.ybar = tk.Scrollbar(self, orient='vertical')
        self.box.config(yscrollcommand=self.ybar.set)
        self.ybar.config(command=self.box.yview)


    def build(self, pack):
        def wrapper(**kwargs):
            pack(kwargs)
            self.box.pack(side='left', fill='y')
            self.ybar.pack(side='right', fill='y')
        return wrapper


    def insert(self, list_items):
        for item, index in zip(list_items, range(len(list_items))):
            instance = item(self.box)
            self.box.create_window(index, 0, window=instance)
            #self.box.insert( '\n')
            instance.pack(anchor='w', fill='x')

            self.ybar.destroy()
            self.ybar = tk.Scrollbar(self)
            self.box.config(yscrollcommand=self.ybar.set)
            self.ybar.config(command=self.box.yview)
            self.ybar.pack(side='right', fill='y')


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')

    objects = []
    s = ShowBox(root)
    s.pack()
    for i in range(15):
        objects.append(ListItem)
        #s.box.insert('end', str(i)+'\n')
        #s.box.window_create('end', window=tk.Label(s.box, text='blablablablablablablablablablablablablablabla').pack())
        #s.box.configure(scrollregion=s('all'))
    s.insert(objects)

    root.mainloop()
