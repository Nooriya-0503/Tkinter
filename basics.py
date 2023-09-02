from tkinter import *


#  Adding two numbers in gui

def add():
    n1 = int(number1.get())
    n2 = int(number2.get())
    answer.config(text=f"Addition of two numbers is {n1 + n2}")


root = Tk()
root.geometry("500x500")
number1 = Entry()
number2 = Entry()
number1.pack()
number2.pack()
button = Button(text="Add", command=add)
button.pack()
answer = Label()
answer.pack()

root.mainloop()
