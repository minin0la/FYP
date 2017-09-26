#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.8.7a
# In conjunction with Tcl version 8.6
#    Jan 16, 2017 06:58:50 PM
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

import fa_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = FotoAlbum (root)
    fa_support.init(root, top)
    root.mainloop()

w = None
def create_FotoAlbum(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = FotoAlbum (w)
    fa_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_FotoAlbum():
    global w
    w.destroy()
    w = None


class FotoAlbum:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#f5deb3'  # X11 color: 'wheat'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2'
        font10 = "-family {DejaVu Sans Mono} -size 14 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("600x460+658+160")
        top.title("FotoAlbum")
        top.configure(background="#f5deb3")
        top.configure(highlightbackground="#f5deb3")
        top.configure(highlightcolor="black")
        top.bind('<Control-Key-KP_Add>',lambda e:fa_support.zoom('in'))
        top.bind('<Control-Key-KP_Subtract>',lambda e:fa_support.zoom('out'))
        top.bind('<Control-Key-a>',lambda e:fa_support.display_dir('arc'))
        top.bind('<Control-Key-i>',lambda e:fa_support.display_dir('inc'))
        top.bind('<Control-Key-minus>',lambda e:fa_support.zoom_out())
        if (root.tk.call('tk', 'windowingsystem')=='aqua'):
            top.bind('<Button-2>', lambda e: self.popup1(e))
            top.bind('<Control-1>', lambda e: self.popup1(e))
        else:
            top.bind('<Button-3>', lambda e: self.popup1(e))
        top.bind('<Control-Key-q>',lambda e:fa_support.quit())
        top.bind('<Control-Key-r>',lambda e:fa_support.refresh())
        top.bind('<Control-Key-s>',lambda e:fa_support.view_archive())
        top.bind('<Control-Key-t>',lambda e:fa_support.toggle_file_name())
        top.bind('<Key-Shift_L><Control-Key-plus>',lambda e:fa_support.zoom_in())
        top.bind('<Key-Shift_R><Control-Key-plus>',lambda e :fa_support.zoom_in())



        self.Custom1 = fa_support.Custom(top)
        self.Custom1.place(relx=0.0, rely=0.0, relheight=0.83, relwidth=1.0)

        self.menubar = Menu(top,font=font10,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.photos = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.photos,
                activebackground="#f4bcb2",
                activeforeground="#111111",
                background="wheat",
                font=font10,
                foreground="#000000",
                label="Photos")
        self.photos.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                accelerator="Cntrl-S",
                background="#d9d9d9",
                command=fa_support.view_archive,
                font=font10,
                foreground="#000000",
                label="Search Archive")
        self.photos.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                accelerator="Cntrl-I",
                background="#d9d9d9",
                command=lambda:fa_support.display_dir('inc'),
                font=font10,
                foreground="#000000",
                label="Incoming directory")
        self.photos.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                accelerator="Cntrl-A",
                background="#d9d9d9",
                command=lambda:fa_support.display_dir('arc'),
                font=font10,
                foreground="#000000",
                label="View Archive directory")
        self.photos.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                accelerator="Cntrl-q",
                background="#d9d9d9",
                command=fa_support.quit,
                font=font10,
                foreground="#000000",
                label="Quit")
        self.actions = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.actions,
                activebackground="#f4bcb2",
                activeforeground="#111111",
                background="wheat",
                font=font10,
                foreground="#000000",
                label="Actions")
        self.zoom = Menu(top,tearoff=0)
        self.actions.add_cascade(menu=self.zoom,
                activebackground="#f4bcb2",
                activeforeground="#111111",
                background="#d9d9d9",
                font=font10,
                foreground="#000000",
                label="Zoom")
        self.zoom.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                accelerator="Cntrl-+",
                background="#d9d9d9",
                command=lambda:fa_support.zoom('in'),
                font=font10,
                foreground="#000000",
                label="Zoom In")
        self.zoom.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                accelerator="Cntrl--",
                background="#d9d9d9",
                command=lambda:fa_support.zoom('out'),
                font=font10,
                foreground="#000000",
                label="Zoom Out")
        self.zoom.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:fa_support.zoom('default'),
                font=font10,
                foreground="#000000",
                label="Default Size")
        self.zoom.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda :fa_support.zoom(300),
                font=font10,
                foreground="#000000",
                label="300x300")
        self.zoom.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda :fa_support.zoom(400),
                font=font10,
                foreground="#000000",
                label="400x400")
        self.zoom.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda :fa_support.zoom(400),
                font=font10,
                foreground="#000000",
                label="500x500")
        self.zoom.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda :fa_support.zoom(600),
                font=font10,
                foreground="#000000",
                label="600x600")
        self.actions.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                accelerator="Cntrl-R",
                background="#d9d9d9",
                command=fa_support.refresh,
                font=font10,
                foreground="#000000",
                label="Refresh")
        self.actions.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=fa_support.display_attributes,
                font=font10,
                foreground="#000000",
                label="Display Attributes")
        self.actions.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                accelerator="Cntrl-T",
                background="#d9d9d9",
                command=fa_support.toggle_file_name,
                font=font10,
                foreground="#000000",
                label="Toggle File Name")
        self.zoom1 = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.zoom1,
                activebackground="#f4bcb2",
                activeforeground="#111111",
                background="wheat",
                font=font10,
                foreground="#000000",
                label="Zoom")
        self.zoom1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                accelerator="Cntrl-+",
                background="#d9d9d9",
                command=lambda:fa_support.zoom('in'),
                font=font10,
                foreground="#000000",
                label="Zoom In")
        self.zoom1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                accelerator="cntrl--",
                background="#d9d9d9",
                command=lambda:fa_support.zoom('out'),
                font=font10,
                foreground="#000000",
                label="Zoom Out")
        self.zoom1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:fa_support.zoom('default'),
                font=font10,
                foreground="#000000",
                label="Default Size")
        self.zoom1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font10,
                foreground="#000000",
                label="300x300")
        self.zoom1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda :fa_support.zoom(400),
                font=font10,
                foreground="#000000",
                label="400x400")
        self.zoom1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font10,
                foreground="#000000",
                label="500x500")
        self.zoom1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font10,
                foreground="#000000",
                label="600x600")
        self.menubar.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=fa_support.quit,
                font=font10,
                foreground="#000000",
                label="Quit")


        self.Button1 = Button(top)
        self.Button1.place(relx=0.42, rely=0.89, height=35, width=70)
        self.Button1.configure(activebackground="#f4bcb2")
        self.Button1.configure(background="#f5deb3")
        self.Button1.configure(command=fa_support.quit)
        self.Button1.configure(disabledforeground="#b8a786")
        self.Button1.configure(font=font10)
        self.Button1.configure(highlightbackground="#f5deb3")
        self.Button1.configure(text='''Quit''')

    @staticmethod
    def popup1(event):
        font10 = "-family {DejaVu Sans Mono} -size 14 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#ffffcd")
        Popupmenu1.configure(background="#f5deb3")
        Popupmenu1.configure(disabledforeground="#b8a786")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#f5deb3",
                command=lambda:fa_support.use_xv(event),
                font="{DejaVu Sans Mono} 12",
                foreground="#000000",
                label="Display using xv")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#f5deb3",
                command=lambda:fa_support.call_geeqie(event),
                font=font10,
                foreground="#000000",
                label="Display using Geeqie")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#f5deb3",
                command=fa_support.add_to_archive,
                font=font10,
                foreground="#000000",
                label="Add to Archive")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#f5deb3",
                font=font10,
                foreground="#000000",
                label="Modify Attributes")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#f5deb3",
                command=lambda:fa_support.show_description(event),
                font=font10,
                foreground="#000000",
                label="Display Description")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#f5deb3",
                command=lambda:fa_support.show_exif(event),
                font=font10,
                foreground="#000000",
                label="Display Exif")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=lambda:fa_support.duplicate_image(event),
                font=font10,
                foreground="#000000",
                label="Duplicate Image")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=lambda:fa_support.export(event),
                font=font10,
                foreground="#000000",
                label="Export")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=lambda:fa_support.delete_image(event),
                font=font10,
                foreground="#000000",
                label="Delete")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=lambda:fa_support.call_gimp(event),
                font=font10,
                foreground="#000000",
                label="Modify using Gimp")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=lambda:fa_support.rotate_images(event, 270),
                font=font10,
                foreground="#000000",
                label="Rotate Clockwise")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=lambda:fa_support.rotate_images(event, 90),
                font=font10,
                foreground="#000000",
                label="Rotate CtrClockwise")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=fa_support.clear_selected_images,
                font=font10,
                foreground="#000000",
                label="Null-Clear Selection")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=fa_support.quit,
                font=font10,
                foreground="#000000",
                label="Quit")
        Popupmenu1.post(event.x_root, event.y_root)

    @staticmethod
    def popup2(event):
        font10 = "-family {DejaVu Sans Mono} -size 14 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        Popupmenu2 = Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#ffffcd")
        Popupmenu2.configure(background="#f5deb3")
        Popupmenu2.configure(disabledforeground="#b8a786")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:fa_support.use_xv(event),
                font=font10,
                foreground="#000000",
                label="Display using xv")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:fa_support.call_geeqie(event),
                font=font10,
                foreground="#000000",
                label="Display using Geeqie")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:fa_support.add_to_archive(event),
                font=font10,
                foreground="#000000",
                label="Add to Archive")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:fa_support.show_exif(event),
                font=font10,
                foreground="#000000",
                label="Show Exif")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:fa_support.duplicate_image(event),
                font=font10,
                foreground="#000000",
                label="Duplicate Image")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:fa_support.call_gimp(event),
                font=font10,
                foreground="#000000",
                label="Modify using Gimp")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:fa_support.rotate_images(event, 270),
                font=font10,
                foreground="#000000",
                label="Rotate Clockwise")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:fa_support.rotate_images(event, 90),
                font=font10,
                foreground="#000000",
                label="Rotate CtrClockwise")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:fa_support.clear_selected_images,
                font=font10,
                foreground="#000000",
                label="Null-ClearSelection")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="#d9d9d9",
                command=fa_support.quit,
                font=font10,
                foreground="#000000",
                label="Quit")
        Popupmenu2.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()


