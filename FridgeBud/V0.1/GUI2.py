#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Sep 18, 2017 03:52:28 PM
import sys

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

import GUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Al Bayan} -size 24 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+461+347")
        top.title("New Toplevel 1")
        top.configure(background="#d9d9d9")



        self.Button1 = Button(top)
        self.Button1.place(relx=0.57, rely=0.67, height=42, width=177)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(text='''FUCK THE WORLD''')
        self.Button1.configure(width=177)
        self.Button1.bind('<Button-1>',lambda e:GUI_support.fuck_the_world_button(e))

        self.Button2 = Button(top)
        self.Button2.place(relx=0.15, rely=0.67, height=42, width=177)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(text='''HELLO WORLD''')
        self.Button2.bind('<Button-1>',lambda e:GUI_support.hello_world_button(e))

        self.TextBox = Label(top)
        self.TextBox.place(relx=0.07, rely=0.13, height=164, width=531)
        self.TextBox.configure(background="#d9d9d9")
        self.TextBox.configure(font=font10)
        self.TextBox.configure(foreground="#000000")
        self.TextBox.configure(width=531)






if __name__ == '__main__':
    vp_start_gui()


