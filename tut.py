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
    frame3 = Frame(win)       # event display
    frame3 = Frame(win)  # select of names
    frame3.pack()
    Label(frame3, text="ID").grid(row=0, column=0, sticky=W)
    scroll1 = Scrollbar(frame3, orient=VERTICAL)
    scroll2 = Scrollbar(frame3, orient=VERTICAL)
    select1 = Listbox(frame3, yscrollcommand=scroll1.set, height=6)
    select2 = Listbox(frame3, yscrollcommand=scroll2.set, height=6)
    scroll1.config(command=select1.yview)
    scroll1.grid(row = 1, column = 0)
    scroll2.config(command=select2.yview)
    scroll2.grid(row = 1, column = 1)
    Label(frame3, text="Event").grid(row=0, column=1, sticky=W)
    select1.grid(row = 1, column = 0)
    select2.grid(row = 1, column = 1)

    #input
    frame2 = Frame(win)
    frame2.pack()

    

    Label(frame2, text="Source-Event").grid(row=2, column=0)
    sour_evt = StringVar()
    evs = Entry(frame2, textvariable=sour_evt)
    evs.grid(row=3, column=0, sticky=W)

    Label(frame2, text="Destination-Event").grid(row=2, column=1, sticky=W)
    dest_evt = StringVar()
    evd = Entry(frame2, textvariable=dest_evt)
    evd.grid(row=3, column=1, sticky=W)

    Label(frame2, text="Source-Timex").grid(row=2, column=2, sticky=W)
    sour_tim = StringVar()
    tvs = Entry(frame2, textvariable=sour_tim)
    tvs.grid(row=3, column=2, sticky=W)

    Label(frame2, text="Destination-Timex").grid(row=2, column=3, sticky=W)
    dest_tim = StringVar()
    tvd = Entry(frame2, textvariable=dest_tim)
    tvd.grid(row=3, column=3, sticky=W)

    Label(frame2, text="Event-Relation").grid(row=2, column=4, sticky=W)
    variable = StringVar()
    variable.set("SUBEVENT") # default value
    w = OptionMenu(frame2, variable,"SUBEVENT", "PURPOSE", "REASON", "ENABLEMENT", "PRECEDENCE", "RELATED")
    w.grid(row=3, column =4, sticky=W)

    Label(frame2, text="Timex-Relation").grid(row=2, column=5, sticky=W)    
    var = StringVar()
    var.set("BEFORE") # default value
    w = OptionMenu(frame2, var,"BEFORE", "AFTER" , "INCLUDES" , "IS_INCLUDED" ,"DURING" , "DURING_INV" , "SIMULTANEOUS" , "IAFTER" , "IBEFORE" ,"IDENTITY" , "BEGINS" , "ENDS" , "BEGUN_BY" , "ENDED_BY")
    w.grid(row=3, column = 5, sticky=W)

    Label(frame2, text="Link-Type").grid(row=2, column=6, sticky=W)    
    var2 = StringVar()
    var2.set("LINK") # default value
    w = OptionMenu(frame2, var2,"LINK","TLINK")
    w.grid(row=3, column = 6, sticky=W)

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
