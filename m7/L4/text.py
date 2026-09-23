from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Text editor")
window.geometry("300x300")
def open_file():
    filename = askopenfilename(filetypes=[("Text Files", "*.txt"), ("allfiles", "*.*")])

    if filename:
        with open(filename, "r") as file:
            text = file.read()
        txt_edit.delete(1.0, END)
        txt_edit.insert(END, text)

def save_file():
    filename = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("allfiles", "*.*")])

    if filename:
        with open(filename, "w") as file:
            text = txt_edit.get(1.0, END)
            file.write(text)

txt_edit = Text(window)
txt_edit.pack()

s = Button(window,text="save", command=save_file)
s.pack()

o = Button(window,text="open", command=open_file)
o.pack()
            
window.mainloop()