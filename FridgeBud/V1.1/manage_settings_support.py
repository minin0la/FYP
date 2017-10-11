#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 04, 2017 03:07:55 PM


import sys
import GUI_support
import popup_text_country
import popup_text_location_1
import popup_text_location_2
from dataIO import fileIO
import subprocess

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

def quit_app():
    GUI_support.destroy_window()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    show_info()

def togglesmallscreen():
    global top_level
    top_level.wm_state("iconic")

def country(value):
    setcountry(value)
    show_info()
    GUI_support.togglebigscreen()
    global top_level
    top_level.wm_state("normal")

def home(value):
    sethome(value)
    show_info()
    GUI_support.togglebigscreen()
    global top_level
    top_level.wm_state("normal")

def location1(value):
    setlocation1(value)
    show_info()
    GUI_support.togglebigscreen()
    global top_level
    top_level.wm_state("normal")

def location2(value):
    setlocation2(value)
    show_info()
    GUI_support.togglebigscreen()
    global top_level
    top_level.wm_state("normal")

def country_cancel():
    GUI_support.togglebigscreen()
    global top_level
    top_level.wm_state("normal")

def home_cancel():
    GUI_support.togglebigscreen()
    global top_level
    top_level.wm_state("normal")

def location1_cancel():
    GUI_support.togglebigscreen()
    global top_level
    top_level.wm_state("normal")

def location2_cancel():
    GUI_support.togglebigscreen()
    global top_level
    top_level.wm_state("normal")

def popup_country():
    togglesmallscreen()
    GUI_support.togglesmallscreen()
    popup_text_country.create_Popup(root)
    toggleKeyboard()

def popup_home():
    togglesmallscreen()
    GUI_support.togglesmallscreen()
    popup_text_country.create_Popup(root)
    toggleKeyboard()

def popup_location_1():
    togglesmallscreen()
    GUI_support.togglesmallscreen()
    popup_text_location_1.create_Popup(root)
    toggleKeyboard()

def popup_location_2():
    togglesmallscreen()
    GUI_support.togglesmallscreen()
    popup_text_location_2.create_Popup(root)
    toggleKeyboard()

def toggleKeyboard():
    p = subprocess.Popen(['florence show'], shell=True, stdout= subprocess.PIPE, stderr= subprocess.PIPE, universal_newlines=True)
    if not "" == p.stderr.readline():
        subprocess.Popen(['florence'], shell=True) 

def setcountry(value):
    settings = fileIO("data/settings.json", "load")
    settings[0]["Country"] = str(value)
    fileIO("data/settings.json", "save", settings)

def sethome(value):
    settings = fileIO("data/settings.json", "load")
    import googlemaps
    gmaps = googlemaps.Client(key='AIzaSyANTUayx1TPQk3pSQX4OMvHdjGuRFI3NWo')
    geocode_result = gmaps.geocode(str(value), {'country': settings[0]["Country"]})
    settings[0]["Home"] = geocode_result[0]["formatted_address"]
    fileIO("data/settings.json", "save", settings)

def setlocation1(value):
    settings = fileIO("data/settings.json", "load")
    import googlemaps
    gmaps = googlemaps.Client(key='AIzaSyANTUayx1TPQk3pSQX4OMvHdjGuRFI3NWo')
    geocode_result = gmaps.geocode(str(value), {'country': settings[0]["Country"]})
    settings[0]["Location 1"] = geocode_result[0]["formatted_address"]
    fileIO("data/settings.json", "save", settings)

def setlocation2(value):
    settings = fileIO("data/settings.json", "load")
    import googlemaps
    gmaps = googlemaps.Client(key='AIzaSyANTUayx1TPQk3pSQX4OMvHdjGuRFI3NWo')
    geocode_result = gmaps.geocode(str(value), {'country': settings[0]["Country"]})
    settings[0]["Location 2"] = geocode_result[0]["formatted_address"]
    fileIO("data/settings.json", "save", settings)

def show_info():
    settings = fileIO("data/settings.json", "load")
    w.current_country_label.configure(text='''{}'''.format(settings[0]["Country"]))
    w.home_label.configure(text='''{}'''.format(settings[0]["Home"]))
    w.current_location_1_label.configure(text='''{}'''.format(settings[0]["Location 1"]))
    w.current_location_2_label.configure(text='''{}'''.format(settings[0]["Location 2"]))

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import manage_settings
    manage_settings.vp_start_gui()

