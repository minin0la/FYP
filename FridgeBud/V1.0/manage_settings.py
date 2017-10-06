#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 04, 2017 03:07:27 PM
import sys
import GUI_support

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
        top.wm_attributes('-fullscreen', 'True')
        top.title("FridgeBud")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.work_set_button = Button(top)
        self.work_set_button.place(relx=0.08, rely=0.22, height=32, width=167)
        self.work_set_button.configure(activebackground="#d9d9d9")
        self.work_set_button.configure(activeforeground="#000000")
        self.work_set_button.configure(background="#d9d9d9")
        self.work_set_button.configure(foreground="#000000")
        self.work_set_button.configure(highlightbackground="#d9d9d9")
        self.work_set_button.configure(highlightcolor="black")
        self.work_set_button.configure(text='''Set Work Location''')

        self.weather_set_button = Button(top)
        self.weather_set_button.place(relx=0.08, rely=0.28, height=32, width=167)

        self.weather_set_button.configure(activebackground="#d9d9d9")
        self.weather_set_button.configure(activeforeground="#000000")
        self.weather_set_button.configure(background="#d9d9d9")
        self.weather_set_button.configure(foreground="#000000")
        self.weather_set_button.configure(highlightbackground="#d9d9d9")
        self.weather_set_button.configure(highlightcolor="black")
        self.weather_set_button.configure(text='''Set Weather Location''')

        self.weather_entry = Entry(top)
        self.weather_entry.place(relx=0.25, rely=0.28, relheight=0.05
                , relwidth=0.28)
        self.weather_entry.configure(background="white")
        self.weather_entry.configure(font="TkFixedFont")
        self.weather_entry.configure(foreground="#000000")
        self.weather_entry.configure(highlightbackground="#d9d9d9")
        self.weather_entry.configure(highlightcolor="black")
        self.weather_entry.configure(insertbackground="black")
        self.weather_entry.configure(selectbackground="#c4c4c4")
        self.weather_entry.configure(selectforeground="black")
        self.weather_entry.configure(width=282)

        self.work_entry = Entry(top)
        self.work_entry.place(relx=0.25, rely=0.22, relheight=0.05
                , relwidth=0.28)
        self.work_entry.configure(background="white")
        self.work_entry.configure(font="TkFixedFont")
        self.work_entry.configure(foreground="#000000")
        self.work_entry.configure(highlightbackground="#d9d9d9")
        self.work_entry.configure(highlightcolor="black")
        self.work_entry.configure(insertbackground="black")
        self.work_entry.configure(selectbackground="#c4c4c4")
        self.work_entry.configure(selectforeground="black")
        self.work_entry.configure(width=282)

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

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.quit_button = Button(top)
        self.quit_button.place(relx=0.61, rely=0.88, height=32, width=167)
        self.quit_button.configure(activebackground="#d9d9d9")
        self.quit_button.configure(activeforeground="#000000")
        self.quit_button.configure(background="#d9d9d9")
        self.quit_button.configure(foreground="#000000")
        self.quit_button.configure(highlightbackground="#d9d9d9")
        self.quit_button.configure(highlightcolor="black")
        self.quit_button.configure(text='''Quit Application''')
        self.quit_button.bind('<Button-1>',lambda e:manage_settings_support.quit_app())

        self.current_work_label = Label(top)
        self.current_work_label.place(relx=0.6, rely=0.22, height=24, width=341)
        self.current_work_label.configure(background="#d9d9d9")
        self.current_work_label.configure(foreground="#000000")
        self.current_work_label.configure(text='''Current Work Location''')
        self.current_work_label.configure(width=341)

        self.current_weather_label = Label(top)
        self.current_weather_label.place(relx=0.6, rely=0.28, height=24
                , width=341)
        self.current_weather_label.configure(activebackground="#f9f9f9")
        self.current_weather_label.configure(activeforeground="black")
        self.current_weather_label.configure(background="#d9d9d9")
        self.current_weather_label.configure(foreground="#000000")
        self.current_weather_label.configure(highlightbackground="#d9d9d9")
        self.current_weather_label.configure(highlightcolor="black")
        self.current_weather_label.configure(text='''Current Weather Location''')






if __name__ == '__main__':
    vp_start_gui()


