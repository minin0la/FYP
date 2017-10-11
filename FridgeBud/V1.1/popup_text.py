#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 10, 2017 06:39:21 PM
import sys
import popup_text_support


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Popup (root)
    popup_text_support.init(root, top)
    root.mainloop()

w = None
def create_Popup(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Popup (w)
    popup_text_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Popup():
    global w
    w.destroy()
    w = None


class Popup:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

            # get screen width and height
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        width = 1024
        height = 121
        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2) - 200
        top.geometry('%dx%d+%d+%d' % (width, height, x, y))
        top.title("Input")
        top.configure(background="#d9d9d9")



        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.02, rely=0.08, relheight=0.22, relwidth=0.97)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=582)

        self.OK = Button(top)
        self.OK.place(relx=0.03, rely=0.5, height=42, width=277)
        self.OK.configure(activebackground="#d9d9d9")
        self.OK.configure(activeforeground="#000000")
        self.OK.configure(background="#d9d9d9")
        self.OK.configure(foreground="#000000")
        self.OK.configure(highlightbackground="#d9d9d9")
        self.OK.configure(highlightcolor="black")
        self.OK.configure(text='''OK''')
        self.OK.configure(width=277)
        self.OK.bind('<Button-1>', lambda e: popup_text_support.manage_item_support(e))

        self.CANCEL = Button(top)
        self.CANCEL.place(relx=0.52, rely=0.5, height=42, width=277)
        self.CANCEL.configure(activebackground="#d9d9d9")
        self.CANCEL.configure(activeforeground="#000000")
        self.CANCEL.configure(background="#d9d9d9")
        self.CANCEL.configure(foreground="#000000")
        self.CANCEL.configure(highlightbackground="#d9d9d9")
        self.CANCEL.configure(highlightcolor="black")
        self.CANCEL.configure(text='''CANCEL''')
        self.CANCEL.configure(width=277)






if __name__ == '__main__':
    vp_start_gui()


