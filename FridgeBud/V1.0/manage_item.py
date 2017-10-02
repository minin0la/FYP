#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Sep 30, 2017 11:15:35 AM
import sys
import GUI
import PIL.Image
import PIL.ImageTk

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

import manage_item_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    manage_item_support.set_Tk_var()
    top = FridgeBud (root)
    manage_item_support.init(root, top)
    root.mainloop()

w = None
def create_FridgeBud(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    manage_item_support.set_Tk_var()
    top = FridgeBud (w)
    manage_item_support.init(w, top, *args, **kwargs)
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
        font10 = "-family {Al Bayan} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1024x600+139+157")
        # wed, heg = top.winfo_screenwidth(), top.winfo_screenheight()
        # top.geometry("%dx%d+0+0" % (wed, heg))
        # wed, heg = top.winfo_screenwidth(), top.winfo_screenheight()
        # top.geometry("%dx%d+0+0" % (wed, heg))
        root.attributes('-fullscreen', True)
        root.overrideredirect(1)
        top.title("FridgeBud")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.day_plus_button = Button(top)
        self.day_plus_button.place(relx=0.75, rely=0.32, height=62, width=97)
        self.day_plus_button.configure(activebackground="#d9d9d9")
        self.day_plus_button.configure(activeforeground="#000000")
        self.day_plus_button.configure(background="#d9d9d9")
        self.day_plus_button.configure(font=font10)
        self.day_plus_button.configure(foreground="#000000")
        self.day_plus_button.configure(highlightbackground="#d9d9d9")
        self.day_plus_button.configure(highlightcolor="black")
        self.day_plus_button.configure(text='''+''')
        self.day_plus_button.configure(width=97)
        self.day_plus_button.bind('<Button-1>',lambda e:manage_item_support.day_plus_button(e))

        self.day_minus_button = Button(top)
        self.day_minus_button.place(relx=0.87, rely=0.32, height=62, width=97)
        self.day_minus_button.configure(activebackground="#d9d9d9")
        self.day_minus_button.configure(activeforeground="#000000")
        self.day_minus_button.configure(background="#d9d9d9")
        self.day_minus_button.configure(font=font10)
        self.day_minus_button.configure(foreground="#000000")
        self.day_minus_button.configure(highlightbackground="#d9d9d9")
        self.day_minus_button.configure(highlightcolor="black")
        self.day_minus_button.configure(relief=RAISED)
        self.day_minus_button.configure(text='''-''')
        self.day_minus_button.configure(width=97)
        self.day_minus_button.bind('<Button-1>',lambda e:manage_item_support.day_minus_button(e))

        self.month_plus_button = Button(top)
        self.month_plus_button.place(relx=0.75, rely=0.43, height=62, width=97)
        self.month_plus_button.configure(activebackground="#d9d9d9")
        self.month_plus_button.configure(activeforeground="#000000")
        self.month_plus_button.configure(background="#d9d9d9")
        self.month_plus_button.configure(font=font10)
        self.month_plus_button.configure(foreground="#000000")
        self.month_plus_button.configure(highlightbackground="#d9d9d9")
        self.month_plus_button.configure(highlightcolor="black")
        self.month_plus_button.configure(relief=RAISED)
        self.month_plus_button.configure(text='''+''')
        self.month_plus_button.configure(width=97)
        self.month_plus_button.bind('<Button-1>',lambda e:manage_item_support.month_plus_button(e))

        self.month_minus_button = Button(top)
        self.month_minus_button.place(relx=0.87, rely=0.43, height=62, width=97)
        self.month_minus_button.configure(activebackground="#d9d9d9")
        self.month_minus_button.configure(activeforeground="#000000")
        self.month_minus_button.configure(background="#d9d9d9")
        self.month_minus_button.configure(font=font10)
        self.month_minus_button.configure(foreground="#000000")
        self.month_minus_button.configure(highlightbackground="#d9d9d9")
        self.month_minus_button.configure(highlightcolor="black")
        self.month_minus_button.configure(relief=RAISED)
        self.month_minus_button.configure(text='''-''')
        self.month_minus_button.configure(width=97)
        self.month_minus_button.bind('<Button-1>',lambda e:manage_item_support.month_minus_button(e))

        self.year_plus_button4 = Button(top)
        self.year_plus_button4.place(relx=0.75, rely=0.55, height=62, width=97)
        self.year_plus_button4.configure(activebackground="#d9d9d9")
        self.year_plus_button4.configure(activeforeground="#000000")
        self.year_plus_button4.configure(background="#d9d9d9")
        self.year_plus_button4.configure(font=font10)
        self.year_plus_button4.configure(foreground="#000000")
        self.year_plus_button4.configure(highlightbackground="#d9d9d9")
        self.year_plus_button4.configure(highlightcolor="black")
        self.year_plus_button4.configure(relief=RAISED)
        self.year_plus_button4.configure(text='''+''')
        self.year_plus_button4.configure(width=97)
        self.year_plus_button4.bind('<Button-1>',lambda e:manage_item_support.year_plus_button(e))

        self.year_minus_button = Button(top)
        self.year_minus_button.place(relx=0.87, rely=0.55, height=62, width=97)
        self.year_minus_button.configure(activebackground="#d9d9d9")
        self.year_minus_button.configure(activeforeground="#000000")
        self.year_minus_button.configure(background="#d9d9d9")
        self.year_minus_button.configure(font=font10)
        self.year_minus_button.configure(foreground="#000000")
        self.year_minus_button.configure(highlightbackground="#d9d9d9")
        self.year_minus_button.configure(highlightcolor="black")
        self.year_minus_button.configure(relief=RAISED)
        self.year_minus_button.configure(text='''-''')
        self.year_minus_button.configure(width=97)
        self.year_minus_button.bind('<Button-1>',lambda e:manage_item_support.year_minus_button(e))

        self.item_info_box = Label(top)
        self.item_info_box.place(relx=0.03, rely=0.05, height=134, width=971)
        self.item_info_box.configure(background="#d9d9d9")
        self.item_info_box.configure(cursor="fleur")
        self.item_info_box.configure(font=font10)
        self.item_info_box.configure(foreground="#000000")
        self.item_info_box.configure(text='''Select the items below''')
        self.item_info_box.configure(width=971)

        self.confirm_button = Button(top)
        self.confirm_button.place(relx=0.75, rely=0.67, height=62, width=97)
        self.confirm_button.configure(activebackground="#66ff66")
        self.confirm_button.configure(activeforeground="#66ff66")
        self.confirm_button.configure(background="#66ff66")
        self.confirm_button.configure(foreground="#66ff66")
        self.confirm_button.configure(highlightbackground="#d9d9d9")
        self.confirm_button.configure(highlightcolor="black")
        self.confirm_button.configure(relief=RAISED)
        self.confirm_button.configure(text='''Confirm''')
        self.confirm_button.configure(width=97)
        self.confirm_button.bind('<Button-1>',lambda e:manage_item_support.confirm_button(e))

        self.clear_button = Button(top)
        self.clear_button.place(relx=0.87, rely=0.67, height=62, width=97)
        self.clear_button.configure(activebackground="#d9d9d9")
        self.clear_button.configure(activeforeground="#000000")
        self.clear_button.configure(background="#fb0106")
        self.clear_button.configure(foreground="#000000")
        self.clear_button.configure(highlightbackground="#d9d9d9")
        self.clear_button.configure(highlightcolor="black")
        self.clear_button.configure(relief=RAISED)
        self.clear_button.configure(text='''Clear''')
        self.clear_button.configure(width=97)
        self.clear_button.bind('<Button-1>',lambda e:manage_item_support.clear_button(e))

        self.milk_button = Button(top)
        self.milk_button.place(relx=0.04, rely=0.32, height=152, width=177)
        self.milk_button.configure(activebackground="#d9d9d9")
        self.milk_button.configure(activeforeground="#000000")
        self.milk_button.configure(anchor=NW)
        self.milk_button.configure(background="#d9d9d9")
        self.milk_button.configure(foreground="#000000")
        self.milk_button.configure(highlightbackground="#d9d9d9")
        self.milk_button.configure(highlightcolor="black")
        img = PIL.Image.open("Milk.jpg")
        img = img.resize((152, 177), PIL.Image.ANTIALIAS)
        self._img1 = PIL.ImageTk.PhotoImage(img)
        self.milk_button.configure(image=self._img1)
        self.milk_button.configure(relief=RAISED)
        self.milk_button.bind('<Button-1>',lambda e:manage_item_support.milk_button(e))

        self.drinks_button = Button(top)
        self.drinks_button.place(relx=0.23, rely=0.32, height=152, width=177)
        self.drinks_button.configure(activebackground="#d9d9d9")
        self.drinks_button.configure(activeforeground="#000000")
        self.drinks_button.configure(background="#d9d9d9")
        self.drinks_button.configure(foreground="#000000")
        self.drinks_button.configure(highlightbackground="#d9d9d9")
        self.drinks_button.configure(highlightcolor="black")
        self.drinks_button.configure(relief=RAISED)
        self.drinks_button.configure(text='''Drinks''')
        img = PIL.Image.open("Images/Drinks.jpeg")
        img = img.resize((152, 177), PIL.Image.ANTIALIAS)
        self._img2 = PIL.ImageTk.PhotoImage(img)
        self.drinks_button.configure(image=self._img2)
        self.drinks_button.bind('<Button-1>',lambda e:manage_item_support.drinks_button(e))

        self.meat_button = Button(top)
        self.meat_button.place(relx=0.43, rely=0.32, height=152, width=177)
        self.meat_button.configure(activebackground="#d9d9d9")
        self.meat_button.configure(activeforeground="#000000")
        self.meat_button.configure(background="#d9d9d9")
        self.meat_button.configure(foreground="#000000")
        self.meat_button.configure(highlightbackground="#d9d9d9")
        self.meat_button.configure(highlightcolor="black")
        self.meat_button.configure(relief=RAISED)
        img = PIL.Image.open("Images/Meat.jpg")
        img = img.resize((152, 177), PIL.Image.ANTIALIAS)
        self._img3 = PIL.ImageTk.PhotoImage(img)
        self.meat_button.configure(image=self._img3)
        self.meat_button.configure(text='''Meat''')
        self.meat_button.bind('<Button-1>',lambda e:manage_item_support.meat_button(e))

        self.fish_button = Button(top)
        self.fish_button.place(relx=0.04, rely=0.58, height=152, width=177)
        self.fish_button.configure(activebackground="#d9d9d9")
        self.fish_button.configure(activeforeground="#000000")
        self.fish_button.configure(background="#d9d9d9")
        self.fish_button.configure(foreground="#000000")
        self.fish_button.configure(highlightbackground="#d9d9d9")
        self.fish_button.configure(highlightcolor="black")
        self.fish_button.configure(relief=RAISED)
        self.fish_button.configure(text='''Fish''')
        img = PIL.Image.open("Images/Fish.jpg")
        img = img.resize((152, 177), PIL.Image.ANTIALIAS)
        self._img4 = PIL.ImageTk.PhotoImage(img)
        self.fish_button.configure(image=self._img4)
        self.fish_button.configure(width=167)
        self.fish_button.bind('<Button-1>',lambda e:manage_item_support.fish_button(e))

        self.vegetables_button = Button(top)
        self.vegetables_button.place(relx=0.23, rely=0.58, height=152, width=177)

        self.vegetables_button.configure(activebackground="#d9d9d9")
        self.vegetables_button.configure(activeforeground="#000000")
        self.vegetables_button.configure(background="#d9d9d9")
        self.vegetables_button.configure(foreground="#000000")
        self.vegetables_button.configure(highlightbackground="#d9d9d9")
        self.vegetables_button.configure(highlightcolor="black")
        self.vegetables_button.configure(relief=RAISED)
        self.vegetables_button.configure(text='''Vegetables''')
        img = PIL.Image.open("Images/Vegetables.jpg")
        img = img.resize((152, 177), PIL.Image.ANTIALIAS)
        self._img5 = PIL.ImageTk.PhotoImage(img)
        self.vegetables_button.configure(image=self._img5)
        self.vegetables_button.bind('<Button-1>',lambda e:manage_item_support.vegetables_button(e))

        self.fruits_button = Button(top)
        self.fruits_button.place(relx=0.43, rely=0.58, height=152, width=177)
        self.fruits_button.configure(activebackground="#d9d9d9")
        self.fruits_button.configure(activeforeground="#000000")
        self.fruits_button.configure(background="#d9d9d9")
        self.fruits_button.configure(foreground="#000000")
        self.fruits_button.configure(highlightbackground="#d9d9d9")
        self.fruits_button.configure(highlightcolor="black")
        self.fruits_button.configure(relief=RAISED)
        self.fruits_button.configure(text='''Fruits''')
        img = PIL.Image.open("Images/Fruits.jpeg")
        img = img.resize((152, 177), PIL.Image.ANTIALIAS)
        self._img6 = PIL.ImageTk.PhotoImage(img)
        self.fruits_button.configure(image=self._img6)
        self.fruits_button.bind('<Button-1>',lambda e:manage_item_support.fruits_button(e))

        self.days_box = Label(top)
        self.days_box.place(relx=0.67, rely=0.35, height=24, width=61)
        self.days_box.configure(background="#d9d9d9")
        self.days_box.configure(foreground="#000000")
        self.days_box.configure(text='''Days''')
        self.days_box.configure(width=61)

        self.number_days_box = Label(top)
        self.number_days_box.place(relx=0.62, rely=0.35, height=24, width=61)
        self.number_days_box.configure(activebackground="#f9f9f9")
        self.number_days_box.configure(activeforeground="black")
        self.number_days_box.configure(background="#d9d9d9")
        self.number_days_box.configure(foreground="#000000")
        self.number_days_box.configure(highlightbackground="#d9d9d9")
        self.number_days_box.configure(highlightcolor="black")
        self.number_days_box.configure(text='''0''')

        self.number_months_box = Label(top)
        self.number_months_box.place(relx=0.62, rely=0.47, height=24, width=61)
        self.number_months_box.configure(activebackground="#f9f9f9")
        self.number_months_box.configure(activeforeground="black")
        self.number_months_box.configure(background="#d9d9d9")
        self.number_months_box.configure(foreground="#000000")
        self.number_months_box.configure(highlightbackground="#d9d9d9")
        self.number_months_box.configure(highlightcolor="black")
        self.number_months_box.configure(text='''0''')

        self.months_box = Label(top)
        self.months_box.place(relx=0.67, rely=0.47, height=24, width=61)
        self.months_box.configure(activebackground="#f9f9f9")
        self.months_box.configure(activeforeground="black")
        self.months_box.configure(background="#d9d9d9")
        self.months_box.configure(foreground="#000000")
        self.months_box.configure(highlightbackground="#d9d9d9")
        self.months_box.configure(highlightcolor="black")
        self.months_box.configure(text='''Months''')

        self.number_years_box = Label(top)
        self.number_years_box.place(relx=0.62, rely=0.58, height=24, width=61)
        self.number_years_box.configure(activebackground="#f9f9f9")
        self.number_years_box.configure(activeforeground="black")
        self.number_years_box.configure(background="#d9d9d9")
        self.number_years_box.configure(foreground="#000000")
        self.number_years_box.configure(highlightbackground="#d9d9d9")
        self.number_years_box.configure(highlightcolor="black")
        self.number_years_box.configure(text='''0''')

        self.years_box = Label(top)
        self.years_box.place(relx=0.67, rely=0.58, height=24, width=61)
        self.years_box.configure(activebackground="#f9f9f9")
        self.years_box.configure(activeforeground="black")
        self.years_box.configure(background="#d9d9d9")
        self.years_box.configure(foreground="#000000")
        self.years_box.configure(highlightbackground="#d9d9d9")
        self.years_box.configure(highlightcolor="black")
        self.years_box.configure(text='''Years''')
        self.years_box.configure(width=61)

        self.home_button = Button(top)
        self.home_button.place(relx=0.87, rely=0.85, height=62, width=97)
        self.home_button.configure(activebackground="#d9d9d9")
        self.home_button.configure(activeforeground="#000000")
        self.home_button.configure(background="#d9d9d9")
        self.home_button.configure(foreground="#000000")
        self.home_button.configure(highlightbackground="#d9d9d9")
        self.home_button.configure(highlightcolor="black")
        self.home_button.configure(relief=RAISED)
        self.home_button.configure(text='''Home''')
        self.home_button.configure(width=97)
        self.home_button.bind('<Button-1>',lambda e:manage_item_support.destroy_window())

        self.other_item_entry = Entry(top)
        self.other_item_entry.place(relx=0.04, rely=0.87, relheight=0.1
                , relwidth=0.36)
        self.other_item_entry.configure(background="white")
        self.other_item_entry.configure(font="TkFixedFont")
        self.other_item_entry.configure(foreground="#000000")
        self.other_item_entry.configure(insertbackground="black")
        self.other_item_entry.configure(textvariable=manage_item_support.other_item_text)
        self.other_item_entry.configure(width=372)

        # self.other_time_entry = ttk.Entry(top)
        # self.other_time_entry.place(relx=0.28, rely=0.13, relheight=0.06, relwidth=0.32)
        # self.other_time_entry.configure(takefocus="")
        # self.other_time_entry.configure(cursor="ibeam")

        self.add_other_button = Button(top)
        self.add_other_button.place(relx=0.43, rely=0.87, height=62, width=177)
        self.add_other_button.configure(activebackground="#66ff66")
        self.add_other_button.configure(activeforeground="#000000")
        self.add_other_button.configure(background="#66ff66")
        self.add_other_button.configure(foreground="#000000")
        self.add_other_button.configure(highlightbackground="#d9d9d9")
        self.add_other_button.configure(highlightcolor="black")
        self.add_other_button.configure(relief=RAISED)
        self.add_other_button.configure(text='''Add Other''')
        self.add_other_button.configure(width=177)
        self.add_other_button.bind('<Button-1>',lambda e:manage_item_support.add_other_button(e))




if __name__ == '__main__':
    vp_start_gui()


