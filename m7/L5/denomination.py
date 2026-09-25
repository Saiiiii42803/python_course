from tkinter import *

index = 0
count = 0
notes = [500, 200, 100, 50, 20, 10, 1]
customer_served = 0
total_amount = 0
remaining = 0


def calculate():
    top = Toplevel(window)
    top.title("denomination result")
    top.geometry("200x200")
    index = 0
    withdrawal = int(entry.get())
    remaining = withdrawal
    while True:
        count = remaining // notes [index]
        if count > 0:
            Label(top, text=f"{count}, x, {notes[index]}, unit note(s)").pack()
            remaining = remaining % notes [index]
        index = index + 1
        if remaining <= 0:
            break


window = Tk()
window.title("denomination calculator")
window.geometry("300x300")
heading = Label(window,text="Denomination Calculator")
heading.pack()
help = Label(window,text="Enter amount")
help.pack()

entry = Entry(window)
entry.pack()

button = Button(window,text="Calculate", command=calculate)
button.pack()

window.mainloop()