import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector


class ListItem(tk.Frame):
    def __init__(self, origin, values):
        super().__init__(origin)
        self.pack = self.build(self.pack)

        # None-Widget stored data
        # DB_Structure: id, titel, artist, publisher, release, placement_Id
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
        self.data_id = values['id']
        self.data_mediatype = values['mediatype']
        self.data_title = tk.Label(self.right_side, text=values['title'], anchor='w', width=59)
        self.data_artist = tk.Label(self.right_side, text=values['artist'], anchor='w', width=59)
        self.data_publisher = tk.Label(self.right_side, text=values['publisher'], anchor='w', width=59)
        self.data_release = tk.Label(self.right_side, text=values['release'], anchor='w', width=59)

        # add and bind staff to event-manager
        self.retag('showbox', self.label_artist, self.label_title, self.label_release, self.label_publisher,
                   self.data_title, self.data_artist, self.data_release, self.data_publisher)
        self.bind_class('showbox', '<Button-1>', self.master.master.master.get_item_details)

    # Building functionality here
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
        db = mysql.connector.connect(user='python', password='', host='192.168.8.15', database='bibo')
        cursor = db.cursor()
        typo = None
        if self.data_mediatype == 'literature':
            typo = 1
        if self.data_mediatype == 'music':
            typo = 2
        if self.data_mediatype == 'movies':
            typo = 3
        query = ('SELECT c.firstname, c.name, l.date_input, l.date_output '
                 'FROM lending AS l '
                 'JOIN customer c ON c.id = l.id_customer '
                 'WHERE l.id_media = %s AND l.id_type = %s;')
        cursor.execute(query, (self.data_id, typo))
        data = cursor.fetchone()
        status = ''
        if (data is None) or (data[2] is not None):
            status = 'available'
        else:
            status = 'lent to ' + data[1] + ', ' + data[0]


        self.generate_toplevel(
            self.data_title['text'],
            self.data_artist['text'],
            self.data_publisher['text'],
            self.data_release['text'],
            status
        )

        cursor.close()
        db.close()

        """return dict(title=self.data_title['text'],
                    artist=self.data_artist['text'],
                    publisher=self.data_publisher['text'],
                    release=self.data_release['text'],
                    placement_id=self.placement_id)"""

    def generate_toplevel(self, title, artist, publisher, release, lent):
        toplevel = tk.Toplevel()
        toplevel.geometry("400x250")
        toplevel.title("Details")
        toplevel.resizable(False, False)
        toplevel.grab_set()
        ttk.Label(toplevel, text='Title:\n' + title).pack(pady=3, padx=10, fill='both', anchor='w')
        ttk.Label(toplevel, text='Artist:\n' + artist).pack(pady=3, padx=10, fill='both', anchor='w')
        ttk.Label(toplevel, text='Pubisher:\n' + publisher).pack(pady=3, padx=10, fill='both', anchor='w')
        ttk.Label(toplevel, text='Release:\n' + release).pack(pady=3, padx=10, fill='both', anchor='w')
        ttk.Label(toplevel, text='Status:\n' + lent).pack(pady=3, padx=10, fill='both', anchor='w')
        toplevel.mainloop()
        return

    # bind inside-elements to parent (or maybe the parent to inside...?)
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
        self.scroll_container = None
        self.y_bar = tk.Scrollbar(self, orient='vertical')
        self.y_bar.config(command=self.box.yview)
        self.box.config(yscrollcommand=self.y_bar.set)

        # own Attributes instancing
        self.item_list = []  # storage for instanced ListItems
        self.data_dict = self.init_new_acddm_data()  # dict that contains lists (for AutoComplete-DropDown-Menu)

    # call tk pack() methods inside wrapper
    def build(self, pack):
        def wrapper(**kwargs):
            pack(kwargs)
            self.box.pack(side='left', fill='y')
            self.y_bar.pack(side='right', fill='y')
        return wrapper

    # function triggered by click event
    def get_item_details(self, event):
        # TODO make db request
        # TODO build fancy details window OR show data in (prepared?) details-container at list_item
        target = event.widget.master.master
        print(target.get_data())
        # return 'some'

    def fill_window(self, data, item=ListItem):
        # avoid messed up data
        if data is None:
            return
        if self.item_list:
            self.clear_window()

        # tk stuff for scrollable container
        self.scroll_container = tk.Frame(self.box)
        self.scroll_container.pack()
        self.box.window_create('end', window=self.scroll_container)

        # make items from data, pass values as dictionary
        for row in data:
            values = dict(id=row[0],
                          title=row[1],
                          artist=row[2],
                          publisher=row[3],
                          release=row[4],
                          placement_id=row[5],
                          mediatype=row[6])
            instance = item(self.scroll_container, values)
            instance.pack(anchor='w')

            # prepare lists for ACDDM and store instance reference
            self.fill_acddm_data(self.data_dict, values)
            self.item_list.append(instance)

    def clear_window(self):
        self.scroll_container.destroy()
        self.data_dict = self.init_new_acddm_data()
        self.item_list = []

    @staticmethod
    def init_new_acddm_data():
        data_dict = {'id': [],  # lists for AutoComplete DropDown Menu
                     'title': [],
                     'artist': [],
                     'publisher': [],
                     'release': [],
                     'placement_id': []}
        return data_dict

    @staticmethod
    def fill_acddm_data(target, value):
        for t_key, v_key in zip(target.keys(), value.keys()):
            target[t_key].append(value[v_key])


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

    t = lambda: s.fill_window(more_data)

    s = ShowBox(root)
    t = lambda: s.fill_window(more_data)

    s.pack(side='left')
    t()
    #s.insert_items(more_data)
    # help(ShowBox)
    tk.Button(root, text='kaputtschlaan', command=s.clear_window).pack()
    tk.Button(root, text='widderuffbaun', command=lambda: s.fill_window(more_data)).pack()
    tk.Button(root, text='gugge dict', command=lambda: print(s.data_dict)).pack()
    tk.Button(root, text='luggi liste', command=lambda: print(s.item_list)).pack()

    root.mainloop()