#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Sep 30, 2017 08:40:38 AM
import sys
import weather
import manage_item

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
    top = FridgeBud (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_FridgeBud(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = FridgeBud (w)
    GUI_support.init(w, top, *args, **kwargs)
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
        font9 = "-family {Al Bayan} -size 24 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1024x600+139+157")
        # wed, heg = top.winfo_screenwidth(), top.winfo_screenheight()
        # top.geometry("%dx%d+0+0" % (wed, heg))
        top.title("FridgeBud")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.weather_button = Button(top)
        self.weather_button.place(relx=0.05, rely=0.62, height=42, width=177)
        self.weather_button.configure(activebackground="#d9d9d9")
        self.weather_button.configure(activeforeground="#000000")
        self.weather_button.configure(background="#d9d9d9")
        self.weather_button.configure(foreground="#000000")
        self.weather_button.configure(highlightbackground="#d9d9d9")
        self.weather_button.configure(highlightcolor="black")
        self.weather_button.configure(text='''Weather''')
        self.weather_button.bind('<Button-1>',lambda e:GUI_support.weather_button(e))

        self.information_box = Label(top)
        self.information_box.place(relx=0.04, rely=0.05, height=254, width=431)
        self.information_box.configure(activebackground="#f9f9f9")
        self.information_box.configure(activeforeground="black")
        self.information_box.configure(background="#d9d9d9")
        self.information_box.configure(font=font9)
        self.information_box.configure(foreground="#000000")
        self.information_box.configure(highlightbackground="#d9d9d9")
        self.information_box.configure(highlightcolor="black")
        self.information_box.configure(text=weather.get_weather())
        self.information_box.configure(width=431)

        self.information_label = Label(top)
        self.information_label.place(relx=0.05, rely=0.55, height=24, width=77)
        self.information_label.configure(activebackground="#f9f9f9")
        self.information_label.configure(activeforeground="black")
        self.information_label.configure(background="#d9d9d9")
        self.information_label.configure(foreground="#000000")
        self.information_label.configure(highlightbackground="#d9d9d9")
        self.information_label.configure(highlightcolor="black")
        self.information_label.configure(text='''Information''')

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.61, rely=0.17, relheight=0.8
                , relwidth=0.37)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)

        self.item_list_box = Label(top)
        self.item_list_box.place(relx=0.65, rely=0.05, height=54, width=221)
        self.item_list_box.configure(activebackground="#f9f9f9")
        self.item_list_box.configure(activeforeground="black")
        self.item_list_box.configure(background="#d9d9d9")
        self.item_list_box.configure(font=font9)
        self.item_list_box.configure(foreground="#000000")
        self.item_list_box.configure(highlightbackground="#d9d9d9")
        self.item_list_box.configure(highlightcolor="black")
        self.item_list_box.configure(text='''Item List''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.database_label = Label(top)
        self.database_label.place(relx=0.05, rely=0.72, height=24, width=67)
        self.database_label.configure(background="#d9d9d9")
        self.database_label.configure(foreground="#000000")
        self.database_label.configure(text='''Database''')

        self.manage_item_button = Button(top)
        self.manage_item_button.place(relx=0.05, rely=0.77, height=42, width=177)

        self.manage_item_button.configure(activebackground="#d9d9d9")
        self.manage_item_button.configure(activeforeground="#000000")
        self.manage_item_button.configure(background="#d9d9d9")
        self.manage_item_button.configure(foreground="#000000")
        self.manage_item_button.configure(highlightbackground="#d9d9d9")
        self.manage_item_button.configure(highlightcolor="black")
        self.manage_item_button.configure(text='''Manage Item''')
        self.manage_item_button.bind('<Button-1>', lambda e:GUI_support.manage())


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()


