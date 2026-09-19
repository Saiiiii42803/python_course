from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Virus scan")
window.geometry("300x300")

def h_k(event):
    print("You pressed", event.char)
window.bind("<Key>", h_k)

button = Button(window, text=("click me"))
buton = Button(window, text=("click me"))

def m1(event):
    print("mouse 1 pressed", event.char)
button.bind("<Button-1>", m1)

def m2(event):
    print("mouse 2 pressed", event.char)
buton.bind("<Button-3>", m2)

button.pack()

buton.pack()



window.mainloop()