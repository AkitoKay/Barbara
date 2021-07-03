import tkinter as tk

def on_frame_click(event):
    print("frame clicked")

def retag(tag, *args):
    '''Add the given tag as the first bindtag for every widget passed in'''
    for widget in args:
        widget.bindtags((tag,) + widget.bindtags())

root = tk.Tk()
a_frame = tk.Frame(root, bg="red", padx=20, pady=20)
a_label = tk.Label(a_frame, text="A Label")
a_button = tk.Button(a_frame, text="click me!")
a_frame.pack()
a_label.pack()
a_button.pack()
#root.protocol("WM_DELETE_WINDOW", root.destroy)
retag("special", a_frame, a_label, a_button)                #here is the magic!
a_frame.bind_class("special", "<Button>", on_frame_click)   #and here...
root.mainloop()