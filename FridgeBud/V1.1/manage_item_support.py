#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Sep 30, 2017 11:16:11 AM


import sys
import os
from dataIO import fileIO
import time
import datetime
import asyncio
import time
import subprocess
import popup_text

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

def set_Tk_var():
    global other_item_text
    other_item_text = StringVar()

def add_other_button(p1):
    global selected
    selected = other_item_text.get()
    w.other_item_entry.delete(0, 'end')
    show_info()

def day_plus_button(p1):
    global days
    days = days + 1
    show_info()

def day_minus_button(p1):
    global days
    if days != 0:
        days = days - 1
    show_info()

def month_plus_button(p1):
    global months
    months = months + 1
    show_info()

def month_minus_button(p1):
    global months
    if months != 0:
        months = months - 1
    show_info()

def year_plus_button(p1):
    global years
    years = years + 1
    show_info()

def year_minus_button(p1):
    global years
    if years != 0:
        years = years - 1
    show_info()

def drinks_button(p1):
    global selected
    selected = "Drinks"
    show_info()

def fish_button(p1):
    global selected
    selected = "Fish"
    show_info()

def fruits_button(p1):
    global selected
    selected = "Fruits"
    show_info()

def home_button(p1):
    print('manage_item_support.home_button')
    sys.stdout.flush()

def meat_button(p1):
    global selected
    selected = "Meats"
    show_info()

def milk_button(p1):
    global selected
    selected = "Milks"
    show_info()

def vegetables_button(p1):
    global selected
    selected = "Vegetables"
    show_info()

def confirm_button(p1):
    global selected, days, months, years
    if selected != None:
        lists = fileIO("data/list.json", "load")
        # day = get_time().isoweekday()
        #nday_list = {"1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday", "6": "Saturday", "7": "Sunday"}
        date = get_time().day
        month = get_time().month
        year = get_time().year
        lists.append({"Name": selected, "Date": date, "Month": month, "Year": year})
        fileIO("data/list.json", "save", lists)
        selected = None
        days = 0
        months = 0
        years = 0
        show_info()
    else:
        w.item_info_box.configure(text='''Please select the item below first!''')


def clear_button(p1):
    global selected, days, months, years
    selected = None
    days = 0
    months = 0
    years = 0
    show_info()

def get_time():
    result = days * 86400
    result = result + months*2592000
    result = result + years*31536000
    result = datetime.date.today() + datetime.timedelta(seconds=result)
    return result

def returnname(value):
    global selected
    selected = value
    show_info()
    global top_level
    top_level.wm_state("zoomed")

def show_info():
    if selected == None:
        w.item_info_box.configure(text='''Select the items below''')
    elif days == 0 and months == 0 and years == 0:
        w.item_info_box.configure(text='''You have selected {}.\nIt will be expiring today'''.format(selected))
    else:
        w.item_info_box.configure(text='''You have selected {}.\nIt will be expiring on {}'''.format(selected, get_time().strftime("%A, %d %B %Y")))

    w.number_days_box.configure(text='''{}'''.format(days))
    w.number_months_box.configure(text='''{}'''.format(months))
    w.number_years_box.configure(text='''{}'''.format(years))

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    main()

def togglesmallscreen():
    global top_level
    top_level.wm_state("iconic")
    # top_level.geometry("320x240")

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def popup():
    togglesmallscreen()
    popup_text.create_Popup(root)
    os.system("matchbox-keyboard")

def toggleKeyboard():
    p = subprocess.Popen(['florence show'], shell=True, stdout= subprocess.PIPE, stderr= subprocess.PIPE, universal_newlines=True)
    if not "" == p.stderr.readline():
        subprocess.Popen(['florence'], shell=True) 


def main():
    global selected, days, months, years
    selected = None
    days = 0
    months = 0
    years = 0
    show_info()

if __name__ == '__main__':
    import manage_item
    manage_item.vp_start_gui()

