import tkinter as tk
import tkinter.ttk as ttk
from functools import partial

class StartWindow:

    def __init__(self, root):
        self.root = root
        self.geometry = root.geometry('200x140')
        self.title = root.title('Options')
        self.resize = root.resizable(False, False)
        self.media_opened = False
        self.lent_opened = False
        self.Mediawindow = None
        self.Lentwindow = None

        self.root.o1 = ttk.Button(text = 'Media', command = self.open_media).pack(padx = 20, pady = 10, side = 'top', fill = 'both')
        self.root.o2 = ttk.Button(text = 'Lent', command = self.open_lent).pack(padx = 20, pady = 10, side = 'top', fill = 'both')
        #self.root.o3 = ttk.Button(text = 'Users').pack(padx = 20, pady = 10, side = 'top', fill = 'both')

    def open_media(self):
        if self.media_opened is False:
            self.media_opened = True
            self.mediawindow = MediaWindow()
            return
        else:
            return

    def open_lent(self):
        pass

class MediaWindow:
    
    def __init__(self):
        self.root = tk.Tk()
        self.title = self.root.title('Media')
        self.geometry = self.root.geometry('800x600')


if __name__ == '__main__':

    start = tk.Tk()
    options = StartWindow(start)
    start.mainloop()

#End of File
