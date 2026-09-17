from tkinter import *

window = Tk()
window.title("Widgets")
window.geometry("300x300")

heading = Label(window,text="Heading")
heading.pack()
name_label = Label(window,text="enter your name")
name_label.pack()
entry = Entry(window)
entry.pack()
button = Button(window,text="This is a button")
button.pack()

window.mainloop()

