#! /usr/bin/env python3
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Sep 30, 2017 08:40:38 AM
import sys
import weather
import json
import PIL.Image
import PIL.ImageTk
import urllib
import traveltime
import os
from dataIO import fileIO

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

# Getting all settings data
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = FridgeBud (root)
    GUI_support.init(root, top)
    root.mainloop()
    # root.overrideredirect(1)

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
        font9 = "-family {Al Bayan} -size 20 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1024x600+139+157")
        top.attributes('-fullscreen', 'True')
        top.title("FridgeBud")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        GUI_support.check_folders()
        GUI_support.check_files()
        settings = fileIO("data/settings.json", "load")
        for i in settings:
            home = i['Home']
            country = i['Country']
            location1 = i['Location 1']
            location2 = i['Location 2']

        self.information_label = Label(top)
        self.information_label.place(relx=0.04, rely=0.58, height=24, width=77)
        self.information_label.configure(activebackground="#f9f9f9")
        self.information_label.configure(activeforeground="black")
        self.information_label.configure(background="#d9d9d9")
        self.information_label.configure(foreground="#000000")
        self.information_label.configure(highlightbackground="#d9d9d9")
        self.information_label.configure(highlightcolor="black")
        self.information_label.configure(text='''Information''')

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.69, rely=0.17, relheight=0.8
                , relwidth=0.29)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)

        self.item_list_box = Label(top)
        self.item_list_box.place(relx=0.73, rely=0.05, height=54, width=221)
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
        self.database_label.place(relx=0.04, rely=0.72, height=24, width=89)
        self.database_label.configure(background="#d9d9d9")
        self.database_label.configure(foreground="#000000")
        self.database_label.configure(text='''Database''')

        self.manage_item_button = Button(top)
        self.manage_item_button.place(relx=0.04, rely=0.77, height=42, width=177)
        self.manage_item_button.configure(activebackground="#d9d9d9")
        self.manage_item_button.configure(activeforeground="#000000")
        self.manage_item_button.configure(background="#66ff66")
        self.manage_item_button.configure(foreground="#000000")
        self.manage_item_button.configure(highlightbackground="#d9d9d9")
        self.manage_item_button.configure(highlightcolor="black")
        self.manage_item_button.configure(text='''Manage Item''')
        self.manage_item_button.bind('<Button-1>', lambda e:GUI_support.manage())

        self.remove_item_button = Button(top)
        self.remove_item_button.place(relx=0.22, rely=0.77, height=42
                , width=177)
        self.remove_item_button.configure(activebackground="#d9d9d9")
        self.remove_item_button.configure(activeforeground="#000000")
        self.remove_item_button.configure(background="#fb0106")
        self.remove_item_button.configure(foreground="#000000")
        self.remove_item_button.configure(highlightbackground="#d9d9d9")
        self.remove_item_button.configure(highlightcolor="black")
        self.remove_item_button.configure(text='''Remove item''')
        self.remove_item_button.bind('<Button-1>',lambda e:GUI_support.remove_item())

        self.send_to_telegram = Button(top)
        self.send_to_telegram.place(relx=0.40, rely=0.77, height=42
                , width=177)
        self.send_to_telegram.configure(activebackground="#d9d9d9")
        self.send_to_telegram.configure(activeforeground="#000000")
        self.send_to_telegram.configure(background="#00bfff")
        self.send_to_telegram.configure(foreground="#000000")
        self.send_to_telegram.configure(highlightbackground="#d9d9d9")
        self.send_to_telegram.configure(highlightcolor="black")
        self.send_to_telegram.configure(text='''Send to Telegram''')
        self.send_to_telegram.bind('<Button-1>',lambda e:GUI_support.send_to_telegram())

        self.setting_button = Button(top)
        self.setting_button.place(relx=0.04, rely=0.9, height=42, width=177)
        self.setting_button.configure(activebackground="#d9d9d9")
        self.setting_button.configure(activeforeground="#000000")
        self.setting_button.configure(background="#ffff00")
        self.setting_button.configure(foreground="#000000")
        self.setting_button.configure(highlightbackground="#d9d9d9")
        self.setting_button.configure(highlightcolor="black")
        self.setting_button.configure(text='''Settings''')
        self.setting_button.bind('<Button-1>',lambda e:GUI_support.settings())

        self.chrome_button = Button(top)
        self.chrome_button.place(relx=0.22, rely=0.9, height=42, width=177)
        self.chrome_button.configure(activebackground="#d9d9d9")
        self.chrome_button.configure(activeforeground="#000000")
        self.chrome_button.configure(background="#ff69b4")
        self.chrome_button.configure(foreground="#000000")
        self.chrome_button.configure(highlightbackground="#d9d9d9")
        self.chrome_button.configure(highlightcolor="black")
        self.chrome_button.configure(text='''Internet''')
        self.chrome_button.bind('<Button-1>',lambda e:GUI_support.chrome())

        self.setting_label = Label(top)
        self.setting_label.place(relx=0.04, rely=0.85, height=24, width=89)
        self.setting_label.configure(activebackground="#f9f9f9")
        self.setting_label.configure(activeforeground="black")
        self.setting_label.configure(background="#d9d9d9")
        self.setting_label.configure(foreground="#000000")
        self.setting_label.configure(highlightbackground="#d9d9d9")
        self.setting_label.configure(highlightcolor="black")
        self.setting_label.configure(text='''Settings''')

        self.weather_icon = Label(top)
        self.weather_icon.place(relx=0.04, rely=0.05, relheight=0.21
                , relwidth=0.14)
        self.weather_icon.configure(activebackground="#f9f9f9")
        self.weather_icon.configure(activeforeground="black")
        self.weather_icon.configure(background="#d9d9d9")
        self.weather_icon.configure(font=font9)
        self.weather_icon.configure(foreground="#000000")
        self.weather_icon.configure(highlightbackground="#d9d9d9")
        self.weather_icon.configure(highlightcolor="black")
        self.weather_icon.configure(anchor=CENTER)
        # icon_path = "Images/weather_icon/" + str(weather.get_weather_icon(country)) + ".gif"
        # img = PIL.Image.open(icon_path)
        # img = img.resize((150, 150), PIL.Image.ANTIALIAS)
        # self._img1 = PIL.ImageTk.PhotoImage(img)
        # self.weather_icon.configure(image=self._img1)
        

        self.weather_location = Label(top)
        self.weather_location.place(relx=0.14, rely=0.05, height=34, width=411)
        self.weather_location.configure(activebackground="#f9f9f9")
        self.weather_location.configure(activeforeground="black")
        self.weather_location.configure(background="#d9d9d9")
        self.weather_location.configure(font=font9)
        self.weather_location.configure(foreground="#000000")
        self.weather_location.configure(highlightbackground="#d9d9d9")
        self.weather_location.configure(highlightcolor="black")
        self.weather_location.configure(justify=LEFT)
        # try:
        #     self.weather_location.configure(text=json.loads(weather.get_observation(country).to_JSON())["Location"]["name"])
        # except:
        #     self.weather_location.configure(text=weather.get_observation(country))
        self.weather_location.configure(width=411)

        self.weather_others = Label(top)
        self.weather_others.place(relx=0.34, rely=0.12, height=94, width=270)
        self.weather_others.configure(activebackground="#f9f9f9")
        self.weather_others.configure(activeforeground="black")
        self.weather_others.configure(background="#d9d9d9")
        self.weather_others.configure(font=font9)
        self.weather_others.configure(foreground="#000000")
        self.weather_others.configure(highlightbackground="#d9d9d9")
        self.weather_others.configure(highlightcolor="black")
        self.weather_others.configure(width=221)
        self.weather_others.configure(justify=LEFT)
        # try:
        #     wind_speed = weather.get_weather(country).get_wind()                  # {'speed': 4.6, 'deg': 330}
        #     humidity = weather.get_weather(country).get_humidity()
        #     status = weather.get_weather(country).get_detailed_status() 
        #     message = "{}\nHumidity: {}%\nWind Speed: {}m/s".format(status, humidity, wind_speed["speed"])
        # except:
        #     message = "Error"
        # self.weather_others.configure(text=message)

        self.traffic_location = Button(top)
        self.traffic_location.place(relx=0.04, rely=0.63, height=42
                , width=107)
        self.traffic_location.configure(activebackground="#d9d9d9")
        self.traffic_location.configure(activeforeground="#000000")
        self.traffic_location.configure(background="#d9d9d9")
        self.traffic_location.configure(foreground="#000000")
        self.traffic_location.configure(highlightbackground="#d9d9d9")
        self.traffic_location.configure(highlightcolor="black")
        self.traffic_location.configure(text='''Location 1''')
        self.traffic_location.configure(width=107)
        self.traffic_location.bind('<Button-1>',lambda e:GUI_support.show_traffic_location_1(e))

        self.traffic_location2 = Button(top)
        self.traffic_location2.place(relx=0.16, rely=0.63, height=42
                , width=107)
        self.traffic_location2.configure(activebackground="#d9d9d9")
        self.traffic_location2.configure(activeforeground="#000000")
        self.traffic_location2.configure(background="#d9d9d9")
        self.traffic_location2.configure(foreground="#000000")
        self.traffic_location2.configure(highlightbackground="#d9d9d9")
        self.traffic_location2.configure(highlightcolor="black")
        self.traffic_location2.configure(text='''Location 2''')
        self.traffic_location2.configure(width=137)
        self.traffic_location2.bind('<Button-1>',lambda e:GUI_support.show_traffic_location_2(e))

        self.traffic_icon = Label(top)
        self.traffic_icon.place(relx=0.04, rely=0.27, relheight=0.30
                , relwidth=0.14)
        self.traffic_icon.configure(background="#d9d9d9")
        self.traffic_icon.configure(highlightbackground="#d9d9d9")
        self.traffic_icon.configure(highlightcolor="black")
        self.traffic_icon.configure(activebackground="#f9f9f9")
        self.traffic_icon.configure(activeforeground="black")
        self.traffic_icon.configure(anchor=CENTER)
        icon_path = "Images/traffic.gif"
        img = PIL.Image.open(icon_path)
        img = img.resize((150, 150), PIL.Image.ANTIALIAS)
        self._img2 = PIL.ImageTk.PhotoImage(img)
        self.traffic_icon.configure(image=self._img2)

        self.traffic_label = Label(top)
        self.traffic_label.place(relx=0.18, rely=0.43, height=34, width=521)
        self.traffic_label.configure(activebackground="#f9f9f9")
        self.traffic_label.configure(activeforeground="black")
        self.traffic_label.configure(background="#d9d9d9")
        # self.traffic_label.configure(font=font9)
        self.traffic_label.configure(foreground="#000000")
        self.traffic_label.configure(highlightbackground="#d9d9d9")
        self.traffic_label.configure(highlightcolor="black")
        self.traffic_label.configure(padx=0)
        self.traffic_label.configure(justify=LEFT)
        

        import tkinter.font
        original_font = tkinter.font.nametofont(self.traffic_label.cget("font"))
        self.custom_font = tkinter.font.Font()
        self.custom_font.configure(**original_font.configure())
        self.traffic_label.configure(font=self.custom_font)

        self.traffic_label_location = Label(top)
        self.traffic_label_location.place(relx=0.18, rely=0.38, height=34, width=521)
        self.traffic_label_location.configure(activebackground="#f9f9f9")
        self.traffic_label_location.configure(activeforeground="black")
        self.traffic_label_location.configure(background="#d9d9d9")
        self.traffic_label_location.configure(foreground="#000000")
        self.traffic_label_location.configure(highlightbackground="#d9d9d9")
        self.traffic_label_location.configure(highlightcolor="black")
        self.traffic_label_location.configure(justify=LEFT)

        original_font2 = tkinter.font.nametofont(self.traffic_label_location.cget("font"))
        self.custom_font2 = tkinter.font.Font()
        self.custom_font2.configure(**original_font2.configure())
        self.traffic_label_location.configure(font=self.custom_font2)
        # self.traffic_label_location.configure(font=("Courier", 44))
        # self.traffic_label_location.configure(width=200)

        # self.traffic_label_location = ScrolledListBox(top)
        # self.traffic_label_location.place(relx=0.22, rely=0.38, relheight=0.032
        #         , relwidth=0.45)
        # self.traffic_label_location.configure(background="white")
        # self.traffic_label_location.configure(font="TkFixedFont")
        # self.traffic_label_location.configure(foreground="black")
        # self.traffic_label_location.configure(highlightbackground="#d9d9d9")
        # self.traffic_label_location.configure(highlightcolor="#d9d9d9")
        # self.traffic_label_location.configure(selectbackground="#c4c4c4")
        # self.traffic_label_location.configure(selectforeground="black")
        # self.traffic_label_location.configure(width=10)
        
        try:
            text, destination = traveltime.get_travel_time()
        except:
            text = "Error"
            destination = "Error"
        self.traffic_length = destination
        self.traffic_status_length = text

        self.weather_temp = Label(top)
        self.weather_temp.place(relx=0.22, rely=0.12, height=94, width=121)
        self.weather_temp.configure(activebackground="#f9f9f9")
        self.weather_temp.configure(activeforeground="black")
        self.weather_temp.configure(background="#d9d9d9")
        self.weather_temp.configure(font=font9)
        self.weather_temp.configure(foreground="#000000")
        self.weather_temp.configure(highlightbackground="#d9d9d9")
        self.weather_temp.configure(highlightcolor="black")
        self.weather_temp.configure(justify=LEFT)
        try:
            temperature = weather.get_weather(country).get_temperature('celsius')['temp']
        except:
            temperature = "Error"
        self.weather_temp.configure(text=str(temperature) + " C")
        self.weather_temp.configure(width=121)

    def traffic_font_size(self):
        text = self.traffic_status_length
        # first, grow the font until the text is too big,
        size = self.custom_font.actual("size")
        size = 521
        self.custom_font.configure(size=size)
        # ... then shrink it until it fits
        size = round((510/self.custom_font.measure(text))*510)
        self.custom_font.configure(size=size)

    def location_font_size(self):
        text = self.traffic_length
        # fi rst, grow the font until the text is too big,
        size = self.custom_font2.actual("size")
        size = 521
        self.custom_font2.configure(size=size)
        # ... then shrink it until it fits
        size = round((510/self.custom_font2.measure(text))*510)
        self.custom_font2.configure(size=size)


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


