from tkinter import *

# Create the main application window
app_window = Tk()
app_window.title("Number Pad")
app_window.geometry("300x400")


# Store the number pad values in a nested list
numbers = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
    ["#", 0, "*"]
]

for c in range(3):
    app_window.columnconfigure(c, weight = 1)

for r in range(4):
    app_window.rowconfigure(r, weight = 1)

for row in range (4):
    for col in range(3):
        num_frame = Frame(app_window, relief=SUNKEN, borderwidth=1)
        num_frame.grid(row=row, column=col)
        num_label = Label(num_frame, text=numbers[row][col])
        num_label.pack(expand=True)

app_window.mainloop()