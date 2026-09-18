from tkinter import *

window = Tk()
window.title("Login/Signup")
window.geometry("300x300")

heading = Label(window,text="Login")
heading.pack()
name_label = Label(window,text="Type Name")
name_label.pack()
entry = Entry(window)
entry.pack()
button = Button(window,text="confirm")
button.pack()

email_label = Label(window,text="Type Email")
email_label.pack()
entry_email = Entry(window)
entry_email.pack()
button_email = Button(window,text="confirm")
button_email.pack()




window.mainloop()

