import tkinter as tk


class ListItem(tk.Frame):
    def __init__(self, origin, values):
        super().__init__(origin)
        self.pack = self.build(self.pack)

        # None-Widget stored data
        # id, titel, artist, publisher, release, placement_Id
        self.view_id = values['view_id']
        self.placement_id = values['placement_id']

        # Container for view-arrangement
        self.left_side = tk.Frame(self)
        self.right_side = tk.Frame(self)

        # Identifier labels
        self.label_title = tk.Label(self.left_side, text='Titel:', anchor='w')
        self.label_artist = tk.Label(self.left_side, text='Artist:', anchor='w')
        self.label_publisher = tk.Label(self.left_side, text='Publisher:', anchor='w')
        self.label_release = tk.Label(self.left_side, text='Release date:', anchor='w')

        # Specific data labels
        self.data_title = tk.Label(self.right_side, text=values['title'], anchor='w', width=59)
        self.data_artist = tk.Label(self.right_side, text=values['artist'], anchor='w', width=59)
        self.data_publisher = tk.Label(self.right_side, text=values['publisher'], anchor='w', width=59)
        self.data_release = tk.Label(self.right_side, text=values['release'], anchor='w', width=59)

        # add and bind inside-stuff to event-manager
        self.retag('showbox', self.label_artist, self.label_title, self.label_release, self.label_publisher,
                   self.data_title, self.data_artist, self.data_release, self.data_publisher)

    #Building functionality here
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

    def get_data(self):
        return dict(view_id=self.view_id,
                    title=self.data_title['text'],
                    artist=self.data_artist['text'],
                    publisher=self.data_publisher['text'],
                    release=self.data_release['text'],
                    placement_id=self.placement_id)


    #bind inside-elements to parent (or maybe the parent to inside...?)
    @staticmethod
    def retag(tag, *args):
        for widget in args:
            widget.bindtags((tag,) + widget.bindtags())


class ShowBox(tk.Frame):
    def __init__(self, origin, **kwargs):
        super().__init__(origin, kwargs)
        self.pack = self.build(self.pack)

        # tk.Widgets instancing
        self.box = tk.Text(self, cursor='arrow')
        self.scroll_container = tk.Frame(self.box)
        self.y_bar = tk.Scrollbar(self, orient='vertical')
        self.y_bar.config(command=self.box.yview)
        self.box.config(yscrollcommand=self.y_bar.set)

        # own Attributes instancing
        self.item_list = []             #store instanced ListItems
        self.data_dict = {'id': [],     #lists for AutoComplete
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
    def get_details(self, event):
        # TODO make db request
        # TODO build fancy details window or show data in (prepared?) details-container at list_item
        target = event.widget.master.master
        print(target.get_data())
        # return 'some'

    def insert(self, data, item=ListItem):
        self.scroll_container.pack()
        self.box.window_create('end', window=self.scroll_container)

        for row, index in zip(data, range(len(data))):
            values = dict(view_id=index,
                          id=row[0],
                          title=row[1],
                          artist=row[2],
                          publisher=row[3],
                          release=row[4],
                          placement_id=row[5])

            instance = item(self.scroll_container, values)
            instance.pack(anchor='w')
            instance.bind_class('showbox', '<Button-1>', self.get_details)
            self.item_list.append(instance)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')

    one_data = ('1',
                'Harry Potter and the Half-Blood Prince (Harry Potter  #6)',
                'J.K. Rowling-Mary GrandPré',
                'Harding Alvin W.',
                '2011-10-23',
                '1')

    more_data = []
    for i in range(15):
        more_data.append(one_data)

    s = ShowBox(root)
    s.pack()
    s.insert(more_data)
    #help(ShowBox)

    root.mainloop()

