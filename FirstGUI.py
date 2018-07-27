import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

# Add a label
a_label = ttk.Label(win, text='A Label')
a_label.grid(column=0, row=0)

# Button click event function
def click_me():
    action.configure(text='@@ I have been clicked @@')
    a_label.configure(foreground='red')
    a_label.configure(text='A Red Label')

# Add a button
action = ttk.Button(win, text='Click me!', command=click_me)
action.grid(column=1, row=0)

win.mainloop()
