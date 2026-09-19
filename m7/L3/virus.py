from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Vius Scan")
window.geometry("300x300")



def virus():
    messagebox.showwarning("ALERT", "virus Found")

buton = Button(window, text=("Virus Scan"), command=virus)

buton.pack()



window.mainloop()