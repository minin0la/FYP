#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 11, 2017 03:38:11 AM
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

import manage_settings_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = FridgeBud (root)
    manage_settings_support.init(root, top)
    root.mainloop()

w = None
def create_FridgeBud(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = FridgeBud (w)
    manage_settings_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_FridgeBud():
    global w
    w.destroy()
    w = None


class FridgeBud:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("1024x600+139+157")
        top.attributes('-fullscreen', 'True')
        top.title("FridgeBud")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        self.home_set = Button(top)
        self.home_set.place(relx=0.08, rely=0.2, height=42, width=167)
        self.home_set.configure(activebackground="#d9d9d9")
        self.home_set.configure(activeforeground="#000000")
        self.home_set.configure(background="#d9d9d9")
        self.home_set.configure(foreground="#000000")
        self.home_set.configure(highlightbackground="#d9d9d9")
        self.home_set.configure(highlightcolor="black")
        self.home_set.configure(text='''Set Home''')
        self.home_set.configure(width=167)
        self.home_set.bind('<Button-1>', lambda e: manage_settings_support.popup_home()) 

        self.Location_1_set = Button(top)
        self.Location_1_set.place(relx=0.08, rely=0.28, height=42, width=167)
        self.Location_1_set.configure(activebackground="#d9d9d9")
        self.Location_1_set.configure(activeforeground="#000000")
        self.Location_1_set.configure(background="#d9d9d9")
        self.Location_1_set.configure(foreground="#000000")
        self.Location_1_set.configure(highlightbackground="#d9d9d9")
        self.Location_1_set.configure(highlightcolor="black")
        self.Location_1_set.configure(text='''Set Location 1''')
        self.Location_1_set.configure(width=167)
        self.Location_1_set.bind('<Button-1>', lambda e: manage_settings_support.popup_location_1())  

        self.Location_2_set = Button(top)
        self.Location_2_set.place(relx=0.08, rely=0.36, height=42, width=167)
        self.Location_2_set.configure(activebackground="#d9d9d9")
        self.Location_2_set.configure(activeforeground="#000000")
        self.Location_2_set.configure(background="#d9d9d9")
        self.Location_2_set.configure(foreground="#000000")
        self.Location_2_set.configure(highlightbackground="#d9d9d9")
        self.Location_2_set.configure(highlightcolor="black")
        self.Location_2_set.configure(text='''Set Location 2''')
        self.Location_2_set.configure(width=167)
        self.Location_2_set.bind('<Button-1>', lambda e: manage_settings_support.popup_location_2()) 

        self.home_button = Button(top)
        self.home_button.place(relx=0.78, rely=0.88, height=32, width=167)
        self.home_button.configure(activebackground="#d9d9d9")
        self.home_button.configure(activeforeground="#000000")
        self.home_button.configure(background="#d9d9d9")
        self.home_button.configure(foreground="#000000")
        self.home_button.configure(highlightbackground="#d9d9d9")
        self.home_button.configure(highlightcolor="black")
        self.home_button.configure(text='''Home''')
        self.home_button.bind('<Button-1>',lambda e:manage_settings_support.destroy_window())

        self.quit_button = Button(top)
        self.quit_button.place(relx=0.61, rely=0.88, height=32, width=167)
        self.quit_button.configure(activebackground="#d9d9d9")
        self.quit_button.configure(activeforeground="#000000")
        self.quit_button.configure(background="#fb0106")
        self.quit_button.configure(foreground="#000000")
        self.quit_button.configure(highlightbackground="#d9d9d9")
        self.quit_button.configure(highlightcolor="black")
        self.quit_button.configure(text='''Quit Application''')
        self.quit_button.bind('<Button-1>',lambda e:manage_settings_support.quit_app())

        self.home_label = Label(top)
        self.home_label.place(relx=0.26, rely=0.22, height=24, width=701)
        self.home_label.configure(activebackground="#f9f9f9")
        self.home_label.configure(activeforeground="black")
        self.home_label.configure(background="#d9d9d9")
        self.home_label.configure(foreground="#000000")
        self.home_label.configure(highlightbackground="#d9d9d9")
        self.home_label.configure(highlightcolor="black")
        self.home_label.configure(text='''Home Location''')
        self.home_label.configure(width=701)

        self.current_location_1_label = Label(top)
        self.current_location_1_label.place(relx=0.26, rely=0.31, height=24, width=701)

        self.current_location_1_label.configure(activebackground="#f9f9f9")
        self.current_location_1_label.configure(activeforeground="black")
        self.current_location_1_label.configure(background="#d9d9d9")
        self.current_location_1_label.configure(foreground="#000000")
        self.current_location_1_label.configure(highlightbackground="#d9d9d9")
        self.current_location_1_label.configure(highlightcolor="black")
        self.current_location_1_label.configure(text='''Current Location 1''')
        self.current_location_1_label.configure(width=701)

        self.current_location_2_label = Label(top)
        self.current_location_2_label.place(relx=0.26, rely=0.4, height=24
                , width=701)
        self.current_location_2_label.configure(activebackground="#f9f9f9")
        self.current_location_2_label.configure(activeforeground="black")
        self.current_location_2_label.configure(background="#d9d9d9")
        self.current_location_2_label.configure(foreground="#000000")
        self.current_location_2_label.configure(highlightbackground="#d9d9d9")
        self.current_location_2_label.configure(highlightcolor="black")
        self.current_location_2_label.configure(text='''Current Location 2''')
        self.current_location_2_label.configure(width=701)

        self.country_set = Button(top)
        self.country_set.place(relx=0.08, rely=0.12, height=42, width=167)
        self.country_set.configure(activebackground="#d9d9d9")
        self.country_set.configure(activeforeground="#000000")
        self.country_set.configure(background="#d9d9d9")
        self.country_set.configure(foreground="#000000")
        self.country_set.configure(highlightbackground="#d9d9d9")
        self.country_set.configure(highlightcolor="black")
        self.country_set.configure(text='''Set Country''')
        self.country_set.bind('<Button-1>', lambda e: manage_settings_support.popup_country()) 

        self.current_country_label = Label(top)
        self.current_country_label.place(relx=0.26, rely=0.13, height=24
                , width=701)
        self.current_country_label.configure(activebackground="#f9f9f9")
        self.current_country_label.configure(activeforeground="black")
        self.current_country_label.configure(background="#d9d9d9")
        self.current_country_label.configure(foreground="#000000")
        self.current_country_label.configure(highlightbackground="#d9d9d9")
        self.current_country_label.configure(highlightcolor="black")
        self.current_country_label.configure(text='''Current Country''')






if __name__ == '__main__':
    vp_start_gui()


