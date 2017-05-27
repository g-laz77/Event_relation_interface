#!/usr/bin/env python3
from tkinter import *
import extract
import json
import pprint
a = 1
bb = 1
# extract.extractor()
def make_window():
    global select1, select2, sour_evt, dest_evt, sour_tim, dest_tim, var2, var1, variable, xml_file, select3, select4
    xml_file = input("Enter XML file name:")
    win = Tk()
    
    
    # pprint.pprint(data)
    # for k in data:
    #     print(k)

    frame3 = Frame(win)       # event display
    frame3 = Frame(win)  # select of names
    frame3.pack()
    
    Label(frame3, text="eID").grid(row=0, column=0, sticky=W)
    scroll1 = Scrollbar(frame3, orient=VERTICAL)
    select1 = Listbox(frame3, yscrollcommand=scroll1.set, height=40)
    scroll1.config(command=select1.yview)
    scroll1.grid(row = 1, column = 0)
    select1.grid(row = 1, column = 0)
    
    
    Label(frame3, text="Event").grid(row=0, column=1, sticky=W)
    scroll2 = Scrollbar(frame3, orient=VERTICAL)
    select2 = Listbox(frame3, yscrollcommand=scroll2.set, height=40)
    scroll2.config(command=select2.yview)
    scroll2.grid(row = 1, column = 1)
    select2.grid(row = 1, column = 1)

    Label(frame3, text="tID").grid(row=0, column=2, sticky=W)
    scroll3 = Scrollbar(frame3, orient=VERTICAL)
    select3 = Listbox(frame3, yscrollcommand=scroll3.set, height=40)
    scroll3.config(command=select3.yview)
    scroll3.grid(row = 1, column = 2)
    select3.grid(row = 1, column = 2)

    Label(frame3, text="Timex").grid(row=0, column=3, sticky=W)
    scroll4 = Scrollbar(frame3, orient=VERTICAL)
    select4 = Listbox(frame3, yscrollcommand=scroll4.set, height=40)
    scroll4.config(command=select4.yview)
    scroll4.grid(row = 1, column = 3)
    select4.grid(row = 1, column = 3)
    
    Label(frame3, text="Text").grid(row=0, column=4, sticky=W)
    scroll5 = Scrollbar(frame3, orient=VERTICAL)
    select5 = Listbox(frame3, yscrollcommand=scroll5.set, height=40, width=30)
    scroll5.config(command=select5.yview)
    scroll5.grid(row = 1, column = 4)
    select5.grid(row = 1, column = 4)
    
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
    variable.set("None") # default value
    w1 = OptionMenu(frame2, variable,"SUBEVENT", "PURPOSE", "REASON", "ENABLEMENT", "PRECEDENCE", "RELATED")
    w1.grid(row=3, column =4, sticky=W)

    Label(frame2, text="Timex-Relation").grid(row=2, column=5, sticky=W)    
    var = StringVar()
    var.set("None") # default value
    w2 = OptionMenu(frame2, var,"BEFORE", "AFTER" , "INCLUDES" , "IS_INCLUDED" ,"DURING" , "DURING_INV" , "SIMULTANEOUS" , "IAFTER" , "IBEFORE" ,"IDENTITY" , "BEGINS" , "ENDS" , "BEGUN_BY" , "ENDED_BY")
    w2.grid(row=3, column = 5, sticky=W)

    Label(frame2, text="Link-Type").grid(row=2, column=6, sticky=W)    
    var2 = StringVar()
    var2.set("None") # default value
    w3 = OptionMenu(frame2, var2,"LINK","TLINK")
    w3.grid(row=3, column = 6, sticky=W)
    
    b1 = Button(frame2, text="Add", command=add_entry)
    b1.grid(row = 4, column = 3, sticky =W)
    return win

def add_entry():
    fpoint = open(xml_file,"a")
    a = 1
    b = 1
    if var2.get() == "LINK":
        fpoint.write("\n<LINK lid=\""+str(a)+"\" relType=\""+variable.get()+"\" eventID=\""+sour_evt.get()+"\" relatedToEvent=\""+dest_evt.get()+"\">")
        a += 1
    else:
        fpoint.write("\n<TLINK lid=\""+str(bb)+"\" relType=\""+var1.get()+"\" eventID=\""+sour_evt.get()+"\" relatedToTime=\""+dest_tim.get()+"\">")
        b += 1
    fpoint.close()
    set_select()

def set_select():
    # phonelist.sort(key=lambda record: record[1])
    
    json_data = extract.extractor(xml_file)
    data = json.loads(json_data)
    
    select1.delete(0, END)
    select2.delete(0, END)
    select3.delete(0, END)
    select4.delete(0, END)
    # for i in data:
    #     print(i)
    d = 0
    for i in data.items():
        name = i[0]
        y = json.dumps(i[1])
        l =  json.loads(y)
        #print(d)
        for k in l.items():

            if k[0] == "eid":
                if d == 0:
                    select1.insert(END, "{0}".format(k[1]))
                    select2.insert(END, "{0}".format(i[0]))
                    d = 1
                else:
                    select3.insert(END, "{0}".format("--"))
                    select4.insert(END, "{0}".format("--"))
                    select1.insert(END, "{0}".format(k[1]))
                    select2.insert(END, "{0}".format(i[0]))
                    d = 1
                
            elif k[0] == "tid":
                    if d == 1:
                        #print("hi")
                        select3.insert(END, "{0}".format(k[1]))
                        select4.insert(END, "{0}".format(i[0]))
                        d = 0
                    
            #ßd = json.dumps(k[1])
            #print(k)
    

    # for fname, lname, phone in phonelist:
    #     select1.insert(END, "{0}".format(lname))
    #     select2.insert(END, "{0}".format(fname))

win = make_window()
set_select()
win.mainloop()
