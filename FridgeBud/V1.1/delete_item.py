#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 02, 2017 05:28:37 PM
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

import delete_item_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    delete_item_support.set_Tk_var()
    top = FridgeBud (root)
    delete_item_support.init(root, top)
    root.mainloop()

w = None
def create_FridgeBud(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    delete_item_support.set_Tk_var()
    top = FridgeBud (w)
    delete_item_support.init(w, top, *args, **kwargs)
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



        self.item_list = ScrolledListBox(top)
        self.item_list.place(relx=0.03, rely=0.1, relheight=0.84, relwidth=0.35)
        self.item_list.configure(background="white")
        self.item_list.configure(font="TkFixedFont")
        self.item_list.configure(foreground="#000000")
        self.item_list.configure(width=362)

        self.item_list_box = Label(top)
        self.item_list_box.place(relx=0.18, rely=0.03, height=34, width=61)
        self.item_list_box.configure(background="#d9d9d9")
        self.item_list_box.configure(foreground="#000000")
        self.item_list_box.configure(text='''Item list''')
        self.item_list_box.configure(width=61)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.item_number_box = Entry(top)
        self.item_number_box.place(relx=0.68, rely=0.22, relheight=0.08
                , relwidth=0.27)
        self.item_number_box.configure(background="white")
        self.item_number_box.configure(font="TkFixedFont")
        self.item_number_box.configure(foreground="#000000")
        self.item_number_box.configure(insertbackground="black")
        self.item_number_box.configure(width=272)
        self.item_number_box.configure(textvariable=delete_item_support.number_box_text)

        self.Num1 = Button(top)
        self.Num1.place(relx=0.67, rely=0.32, height=62, width=87)
        self.Num1.configure(activebackground="#d9d9d9")
        self.Num1.configure(activeforeground="#000000")
        self.Num1.configure(background="#d9d9d9")
        self.Num1.configure(foreground="#000000")
        self.Num1.configure(highlightbackground="#d9d9d9")
        self.Num1.configure(highlightcolor="black")
        self.Num1.configure(text='''1''')
        self.Num1.configure(width=87)
        self.Num1.bind('<Button-1>',lambda e:delete_item_support.Num1(e))

        self.Num2 = Button(top)
        self.Num2.place(relx=0.77, rely=0.32, height=62, width=87)
        self.Num2.configure(activebackground="#d9d9d9")
        self.Num2.configure(activeforeground="#000000")
        self.Num2.configure(background="#d9d9d9")
        self.Num2.configure(foreground="#000000")
        self.Num2.configure(highlightbackground="#d9d9d9")
        self.Num2.configure(highlightcolor="black")
        self.Num2.configure(text='''2''')
        self.Num2.bind('<Button-1>',lambda e:delete_item_support.Num2(e))

        self.Num3 = Button(top)
        self.Num3.place(relx=0.87, rely=0.32, height=62, width=87)
        self.Num3.configure(activebackground="#d9d9d9")
        self.Num3.configure(activeforeground="#000000")
        self.Num3.configure(background="#d9d9d9")
        self.Num3.configure(foreground="#000000")
        self.Num3.configure(highlightbackground="#d9d9d9")
        self.Num3.configure(highlightcolor="black")
        self.Num3.configure(text='''3''')
        self.Num3.bind('<Button-1>',lambda e:delete_item_support.Num3(e))

        self.Num4 = Button(top)
        self.Num4.place(relx=0.67, rely=0.43, height=62, width=87)
        self.Num4.configure(activebackground="#d9d9d9")
        self.Num4.configure(activeforeground="#000000")
        self.Num4.configure(background="#d9d9d9")
        self.Num4.configure(foreground="#000000")
        self.Num4.configure(highlightbackground="#d9d9d9")
        self.Num4.configure(highlightcolor="black")
        self.Num4.configure(text='''4''')
        self.Num4.bind('<Button-1>',lambda e:delete_item_support.Num4(e))

        self.Num5 = Button(top)
        self.Num5.place(relx=0.77, rely=0.43, height=62, width=87)
        self.Num5.configure(activebackground="#d9d9d9")
        self.Num5.configure(activeforeground="#000000")
        self.Num5.configure(background="#d9d9d9")
        self.Num5.configure(foreground="#000000")
        self.Num5.configure(highlightbackground="#d9d9d9")
        self.Num5.configure(highlightcolor="black")
        self.Num5.configure(text='''5''')
        self.Num5.bind('<Button-1>',lambda e:delete_item_support.Num5(e))

        self.Num6 = Button(top)
        self.Num6.place(relx=0.87, rely=0.43, height=62, width=87)
        self.Num6.configure(activebackground="#d9d9d9")
        self.Num6.configure(activeforeground="#000000")
        self.Num6.configure(background="#d9d9d9")
        self.Num6.configure(foreground="#000000")
        self.Num6.configure(highlightbackground="#d9d9d9")
        self.Num6.configure(highlightcolor="black")
        self.Num6.configure(text='''6''')
        self.Num6.bind('<Button-1>',lambda e:delete_item_support.Num6(e))

        self.Num7 = Button(top)
        self.Num7.place(relx=0.67, rely=0.55, height=62, width=87)
        self.Num7.configure(activebackground="#d9d9d9")
        self.Num7.configure(activeforeground="#000000")
        self.Num7.configure(background="#d9d9d9")
        self.Num7.configure(foreground="#000000")
        self.Num7.configure(highlightbackground="#d9d9d9")
        self.Num7.configure(highlightcolor="black")
        self.Num7.configure(text='''7''')
        self.Num7.bind('<Button-1>',lambda e:delete_item_support.Num7(e))

        self.Num8 = Button(top)
        self.Num8.place(relx=0.77, rely=0.55, height=62, width=87)
        self.Num8.configure(activebackground="#d9d9d9")
        self.Num8.configure(activeforeground="#000000")
        self.Num8.configure(background="#d9d9d9")
        self.Num8.configure(foreground="#000000")
        self.Num8.configure(highlightbackground="#d9d9d9")
        self.Num8.configure(highlightcolor="black")
        self.Num8.configure(text='''8''')
        self.Num8.bind('<Button-1>',lambda e:delete_item_support.Num8(e))

        self.Num9 = Button(top)
        self.Num9.place(relx=0.87, rely=0.55, height=62, width=87)
        self.Num9.configure(activebackground="#d9d9d9")
        self.Num9.configure(activeforeground="#000000")
        self.Num9.configure(background="#d9d9d9")
        self.Num9.configure(foreground="#000000")
        self.Num9.configure(highlightbackground="#d9d9d9")
        self.Num9.configure(highlightcolor="black")
        self.Num9.configure(text='''9''')
        self.Num9.bind('<Button-1>',lambda e:delete_item_support.Num9(e))

        self.Num0 = Button(top)
        self.Num0.place(relx=0.77, rely=0.67, height=62, width=87)
        self.Num0.configure(activebackground="#d9d9d9")
        self.Num0.configure(activeforeground="#000000")
        self.Num0.configure(background="#d9d9d9")
        self.Num0.configure(foreground="#000000")
        self.Num0.configure(highlightbackground="#d9d9d9")
        self.Num0.configure(highlightcolor="black")
        self.Num0.configure(text='''0''')
        self.Num0.bind('<Button-1>',lambda e:delete_item_support.Num0(e))

        self.clear_button = Button(top)
        self.clear_button.place(relx=0.67, rely=0.67, height=62, width=87)
        self.clear_button.configure(activebackground="#d9d9d9")
        self.clear_button.configure(activeforeground="#000000")
        self.clear_button.configure(background="#d9d9d9")
        self.clear_button.configure(foreground="#000000")
        self.clear_button.configure(highlightbackground="#d9d9d9")
        self.clear_button.configure(highlightcolor="black")
        self.clear_button.configure(text='''Clear''')
        self.clear_button.bind('<Button-1>',lambda e:delete_item_support.clear_button(e))

        self.enter_button = Button(top)
        self.enter_button.place(relx=0.87, rely=0.67, height=62, width=87)
        self.enter_button.configure(activebackground="#d9d9d9")
        self.enter_button.configure(activeforeground="#000000")
        self.enter_button.configure(background="#d9d9d9")
        self.enter_button.configure(foreground="#000000")
        self.enter_button.configure(highlightbackground="#d9d9d9")
        self.enter_button.configure(highlightcolor="black")
        self.enter_button.configure(text='''Enter''')
        self.enter_button.bind('<Button-1>',lambda e:delete_item_support.enter_button(e))

        self.home_button = Button(top)
        self.home_button.place(relx=0.87, rely=0.82, height=62, width=87)
        self.home_button.configure(activebackground="#d9d9d9")
        self.home_button.configure(activeforeground="#000000")
        self.home_button.configure(background="#d9d9d9")
        self.home_button.configure(foreground="#000000")
        self.home_button.configure(highlightbackground="#d9d9d9")
        self.home_button.configure(highlightcolor="black")
        self.home_button.configure(text='''Home''')
        self.home_button.bind('<Button-1>',lambda e:delete_item_support.destroy_window())

        self.item_status_box = Label(top)
        self.item_status_box.place(relx=0.41, rely=0.12, height=484, width=241)
        self.item_status_box.configure(background="#d9d9d9")
        self.item_status_box.configure(foreground="#000000")
        self.item_status_box.configure(text='''Label''')
        self.item_status_box.configure(width=241)

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


