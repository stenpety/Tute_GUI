import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

# Add a label
a_label = ttk.Label(win, text='Enter your name: ')
a_label.grid(column=0, row=0)


# Button click event function
def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + )


# Textbox entry
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()  # Gives focus to text box


# Add a button
action = ttk.Button(win, text='Click me!', command=click_me)
action.grid(column=2, row=1)
# action.configure(state='disabled')  # Disables button


# Add a combo box
ttk.Label(win, text='Choose a number: ').grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)


win.mainloop()
