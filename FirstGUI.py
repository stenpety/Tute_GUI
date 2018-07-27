import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

# Add a label
a_label = ttk.Label(win, text='Enter your name: ')
a_label.grid(column=0, row=0)

# Button click event function
def click_me():
    action.configure(text='Hello ' + name.get())


# Textbox entry
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=1, row=0)


# Add a button
action = ttk.Button(win, text='Click me!', command=click_me)
action.grid(column=1, row=1)




win.mainloop()
