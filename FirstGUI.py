import tkinter as tk
from tkinter import ttk


# Add a label
def create_label(win):
    a_label = ttk.Label(win, text='Enter your name: ')
    a_label.grid(column=0, row=0)
    return a_label


# Button click event function
def click_me():
    print("Clicked")
    # action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())


# Textbox entry
def create_textbox(win):
    name = tk.StringVar()
    name_entered = ttk.Entry(win, width=12, textvariable=name)
    name_entered.grid(column=0, row=1)
    name_entered.focus()  # Gives focus to text box
    return name_entered


# Add a button
def create_button(win):
    action = ttk.Button(win, text='Click me!', command=click_me)
    action.grid(column=2, row=1)
    # action.configure(state='disabled')  # Disables button
    return action


# Add a combo box
def create_combobox(win):
    ttk.Label(win, text='Choose a number: ').grid(column=1, row=0)
    number = tk.StringVar()
    number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
    number_chosen['values'] = (1, 2, 4, 42, 100)
    number_chosen.grid(column=1, row=1)
    number_chosen.current(0)
    return number_chosen


def main():
    win = tk.Tk()
    win.title('Python GUI')

    a_label = create_label(win)
    name_entered = create_textbox(win)
    action = create_button(win)
    number_chosen = create_combobox(win)

    win.mainloop()


if __name__ == '__main__':
    main()
