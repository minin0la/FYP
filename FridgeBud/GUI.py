# from Tkinter import *
from Tkinter import*
import time

root = Tk()
text_Input = StringVar()
operator = ""


class GUI(Tk):
    root.geometry("1600x800+0+0")
    root.title("FridgeBud")


tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)
# ================================TIME==========================================
localtime = time.asctime(time.localtime(time.time()))
# ================================Info==========================================
lblInfo = Label(tops, font=('arial', 50, 'bold'), text="FridgeBud",
                fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label(tops, font=('arial', 50, 'bold'), text=localtime,
                fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)
# =============================Calculator=======================================


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input,
                   bd=30, insertwidth=4, bg="powder blue", justify='right')

txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="7", bg="powder blue", command=lambda: btnClick(
        7)).grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="8", bg="powder blue", command=lambda: btnClick(
        8)).grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="9", bg="powder blue", command=lambda: btnClick(
        9)).grid(row=2, column=2)

Addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="+", bg="powder blue", command=lambda: btnClick(
        "+")).grid(row=2, column=3)


root.mainloop()
