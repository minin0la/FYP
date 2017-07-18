# This will be use for GUI of the software
# !/usr/bin/python
import Tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()

root = tk.Tk()


class FridgeBud_tk(tk.Tk):
    root.title("FridgeBud")
    root.geometry("1920x1080")


cv = tk.Canvas(root, width=1920, height=1080)
cv.pack()

photo1 = ImageTk.PhotoImage(Image.open
                            ("/Users/kennethwong/Desktop/FYP/Milk.JPG"))
photo2 = ImageTk.PhotoImage(Image.open
                            ("/Users/kennethwong/Desktop/FYP/Fruits.JPeG"))
photo3 = ImageTk.PhotoImage(Image.open
                            ("/Users/kennethwong/Desktop/FYP/Vegetables.JPG"))
photo4 = ImageTk.PhotoImage(Image.open
                            ("/Users/kennethwong/Desktop/FYP/Fish.JPG"))
photo5 = ImageTk.PhotoImage(Image.open
                            ("/Users/kennethwong/Desktop/FYP/Meat.JPG"))
photo6 = ImageTk.PhotoImage(Image.open
                            ("/Users/kennethwong/Desktop/FYP/Drinks.JPeG"))

cv.create_image(170, 170, image=photo1, anchor='center')
cv.create_image(170, 500, image=photo2, anchor='center')
cv.create_image(600, 200, image=photo3, anchor='center')
cv.create_image(630, 500, image=photo4, anchor='center')
cv.create_image(1050, 200, image=photo5, anchor='center')
cv.create_image(1050, 500, image=photo6, anchor='center')
root.mainloop()
