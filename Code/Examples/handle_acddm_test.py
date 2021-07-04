import tkinter as tk
from Code.Examples.Showbox import ShowBox
from Code.Examples.AutocompeteDropdown import AutocompleteCombobox as Acddm

'''
my_dict = {
   'key_one': [1,6,2,3],
   'key_two': [4,1,9,7],
   'key_three': [1,2,4,3],
}


def parallel_sort(d, key):
    index_order = [i for i, _ in sorted(enumerate(d[key]), key=lambda x: x[1])]
    return {k: [v[i] for i in index_order] for k, v in d.items()}

print(parallel_sort(my_dict, 'key_three'))

### 


a={'a':[i for i in range(10)],'b':[i for i in range(10, 0 , -1)]}
sorted(a.values(), key= lambda x: x[0], reverse=True)
--> [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
sorted(a.values(), key= lambda x: x[0], reverse=False)
--> [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]

c={'a':['d','a','c','b'],'b':['a','b','c','d']}
sorted(c.values(), key= lambda x: x[0], reverse=False)
--> [['a', 'b', 'c', 'd'], ['d', 'a', 'c', 'b']]
sorted(c.values(), key= lambda x: x[1], reverse=False)
--> [['d', 'a', 'c', 'b'], ['a', 'b', 'c', 'd']]
'''

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')

    data = [('1', 'Harry Potter and the Half-Blood Prince (Harry Potter  #6)',
            'J.K. Rowling-Mary GrandPré', 'Harding Alvin W.', '2011-10-23', '1'),
            ('13', "The Ultimate Hitchhiker's Guide (Hitchhiker's Guide to the Galaxy #1-5)",
             'Douglas Adams','Kline Abraham W.','1995-07-27','1'),
            ('14','A Short History of Nearly Everything','Bill Bryson-William Roberts','Mason Ian C.','1978-02-04','1')]

    more_data = []
    for i in range(15):
        more_data+=(data)

    t = lambda: s.fill_window(more_data)

    s = ShowBox(root)
    t = lambda: s.fill_window(more_data)

    s.pack(side='left')
    t()
    #s.insert_items(more_data)
    # help(ShowBox)

    show_some = 'title'

    def switch_menu(show_some):
        if show_some == 'title':
            show_some = 'artist'
        else:
            show_some = 'title'
        acddm.set_completion_list(s.data_dict[show_some])

    acddm = Acddm(root)
    acddm.set_completion_list(s.data_dict[show_some])
    acddm.pack()
    acddm.focus_set()

    def delete_stuff():
        s.clear_window()
        acddm.set_completion_list(s.data_dict[show_some])

    tk.Button(root, text='nich die mama', command= lambda: switch_menu(show_some)).pack()
    tk.Button(root, text='kaputtschlaan', command=delete_stuff).pack()
    tk.Button(root, text='widderuffbaun', command=lambda: s.fill_window(more_data)).pack()
    tk.Button(root, text='gugge dict', command=lambda: print(s.data_dict)).pack()
    tk.Button(root, text='luggi liste', command=lambda: print(s.item_list)).pack()

    acddm.bind('<Return>', lambda event: print(acddm.current()))
    acddm.bind('<Escape>', lambda event: delete_stuff())
    root.mainloop()