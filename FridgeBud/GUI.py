# This will be use for GUI of the software
# !/usr/bin/python
import Tkinter as tk


class FridgeBud_tk(tk.Tk):
    root.title("FridgeBud")
    root.geometry("1920x1080")
    root = tk.Tk()
    photo = tk.PhotoImage(file=r"/Users/kennethwong/Desktop/FYP")


cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(10, 10, image='Milk', anchor='nw')
root.mainloop()
