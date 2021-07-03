import tkinter as tk
#id, titel, artist, publisher, release, palcementId


class ListItem(tk.Frame):
    def __init__(self, root=None):
        tk.Frame.__init__(self, root)
        self.pack = self.build(self.pack)

        self.left_side = tk.Frame(self)
        self.right_side = tk.Frame(self)

        #Identifier labels
        self.labl_titel = tk.Label(self.left_side, text='Titel:', anchor='w')
        self.labl_artist = tk.Label(self.left_side, text='Artist:', anchor='w')
        self.labl_publisher = tk.Label(self.left_side, text='Publisher:', anchor='w')
        self.labl_release = tk.Label(self.left_side, text='Release date:', anchor='w')

        #Specific data labels
        self.data_titel = tk.Label(self.right_side, text='some', anchor='w')
        self.data_artist = tk.Label(self.right_side, text='text', anchor='w')
        self.data_publisher = tk.Label(self.right_side, text='for', anchor='w')
        self.data_release = tk.Label(self.right_side, text='instance', anchor='w')


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


if __name__ == '__main__':
    s = ListItem().pack()
