# This will be use for GUI of the software
# !/usr/bin/python
import Tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()


class FridgeBud_tk(tk.Tk):
    root.title("FridgeBud")
    root.geometry("1920x1080")


photo = ImageTk.PhotoImage(Image.open("/Users/minin0la/Documents/GIt/FYP/FridgeBud/Milk.JPG"))
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(10, 10, image=photo, anchor='nw')
root.mainloop()
