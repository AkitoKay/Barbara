import tkinter as tk


# id, titel, artist, publisher, release, placement_Id

class ListItem(tk.Frame):
    def __init__(self, origin, testvarx=0):
        tk.Frame.__init__(self, origin)
        self.pack = self.build(self.pack)

        self.testvar = testvarx

        # Container for orga
        self.left_side = tk.Frame(self)
        self.right_side = tk.Frame(self)

        # Identifier labels
        self.label_title = tk.Label(self.left_side, text='Titel:', anchor='w')
        self.label_artist = tk.Label(self.left_side, text='Artist:', anchor='w')
        self.label_publisher = tk.Label(self.left_side, text='Publisher:', anchor='w')
        self.label_release = tk.Label(self.left_side, text='Release date:', anchor='w')

        # Specific data labels
        self.data_title = tk.Label(self.right_side, text='some', anchor='w', width=59)
        self.data_artist = tk.Label(self.right_side, text='text', anchor='w', width=59)
        self.data_publisher = tk.Label(self.right_side, text='for', anchor='w', width=59)
        self.data_release = tk.Label(self.right_side, text='instance', anchor='w', width=59)

        # add inside-stuff to eventmanager and bind
        self.retag('showbox', self.label_artist, self.label_title, self.label_release, self.label_publisher,
                   self.data_title, self.data_artist, self.data_release, self.data_publisher)
        self.bind_class('showbox', '<Button-1>', self.get_details)


    def build(self, pack):
        def wrapper(**kwargs):
            pack(kwargs)

            self.left_side.pack(side='left', fill='x')
            self.label_title.pack(fill='x')
            self.label_artist.pack(fill='x')
            self.label_publisher.pack(fill='x')
            self.label_release.pack(fill='x')

            self.right_side.pack(side='right')
            self.data_title.pack(fill='x')
            self.data_artist.pack(fill='x')
            self.data_publisher.pack(fill='x')
            self.data_release.pack(fill='x')

        return wrapper

    def retag(self, tag, *args):
        for widget in args:
            widget.bindtags((tag,) + widget.bindtags())


    def get_details(self, event):
        # TODO read event.widget data
        # TODO make db request
        # TODO build fancy details window or show data in (prepared?) details-container at list_item
        print(event.widget.master.master.testvar)
        print(self.testvar) #didn´t work
        #return 'some'

class ShowBox(tk.Frame):
    def __init__(self, origin, **kwargs):
        tk.Frame.__init__(self, origin, kwargs)
        self.pack = self.build(self.pack)

        # tk.Widgets instancing
        self.box = tk.Text(self, cursor='arrow')
        self.scroll_container = tk.Frame(self.box)
        self.y_bar = tk.Scrollbar(self, orient='vertical')
        self.y_bar.config(command=self.box.yview)
        self.box.config(yscrollcommand=self.y_bar.set)

        # own Attributes instancing
        self.item_list = []
        self.data_dict = {'id': [],
                          'titel': [],
                          'artist': [],
                          'release': []}

    # call tk pack() methods inside wrapper
    def build(self, pack):
        def wrapper(**kwargs):
            pack(kwargs)
            self.box.pack(side='left', fill='y')
            self.y_bar.pack(side='right', fill='y')

        return wrapper

    # own functions defined here
    def insert(self, list_items, i):
        self.scroll_container.pack()
        self.box.window_create('end', window=self.scroll_container)

        for Item in list_items:
            instance: ListItem = Item(self.scroll_container, i)
            #instance.bind('<Button-1>', self.get_details)
            instance.pack(anchor='w', fill='x')
            i -= 1
            self.item_list.append(instance)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')

    objects = []
    s = ShowBox(root)
    s.pack()
    for i in range(15):
        objects.append(ListItem)
        # s.box.insert('end', str(i)+'\n')
        # s.box.window_create('end', window=tk.Label(s.box, text='blablablablablablablablablablablablablablabla').pack())
        # s.box.configure(scrollregion=s('all'))
    s.insert(objects, i)


    root.mainloop()
