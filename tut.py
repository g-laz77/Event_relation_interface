#!/usr/bin/env python3
from tkinter import *

phonelist = [['Chris', 'Meyers', '241-343-4349'],
             ['Robert', 'Smith', '202-689-1234'],
             ['Janet', 'Jones', '609-483-5432'],
             ['Ralph', 'Barnhart', '215-683-2341'],
             ['Eric', 'Nelson', '571-485-2689'],
             ['Ford', 'Prefect', '703-987-6543'],
             ['Mary', 'Zigler', '812-567-8901'],
             ['Bob', 'Smith', '856-689-1234']]


def make_window():
    global select1, select2
    win = Tk()
    frame3 = Frame(win)  # select of names
    frame3.pack()
    Label(frame3, text="ID").grid(row=0, column=0, sticky=W)
    scroll1 = Scrollbar(frame3, orient=VERTICAL)
    scroll2 = Scrollbar(frame3, orient=VERTICAL)
    select1 = Listbox(frame3, yscrollcommand=scroll1.set, height=6)
    select2 = Listbox(frame3, yscrollcommand=scroll2.set, height=6)
    scroll1.config(command=select1.yview)
    scroll1.pack(side=RIGHT, fill=Y)
    scroll2.config(command=select2.yview)
    scroll2.pack(side=RIGHT, fill=Y)
    Label(frame3, text="Event").grid(row=0, column=1, sticky=W)
    select1.pack(side=LEFT, fill=BOTH, expand=1)
    select2.pack(side=RIGHT, fill=BOTH, expand=1)
    return win


def set_select():
    phonelist.sort(key=lambda record: record[1])
    select1.delete(0, END)
    select2.delete(0, END)

    for fname, lname, phone in phonelist:
        select1.insert(END, "{0}".format(lname))
        select2.insert(END, "{0}".format(fname))


win = make_window()
set_select()
win.mainloop()
