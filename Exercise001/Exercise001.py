# GeekBrains intermediate assessment Exercise001
# Create a notes app

import os
import json
from datetime import date
from datetime import time
from datetime import datetime
import platform
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter.messagebox import showinfo, askyesno
from Add import add
from Edit import editor

data = json.load(open('Exercise001/Notes.json'))

id = 0

if platform.system() == 'Windows':
    name = os.environ.get('USERNAME')
elif platform.system() == 'Darwin':
    name = os.environ.get('USER')

print(f'Hello, {name}!')

def main():
    def help():
        showhelp = ('Filter by date -> show notes under specified date\n \
                    New note -> write a new note\n \
                    Editor -> edit existing note\n \
                    Refresh - refresh list of notes\n \
                    Exit - close program')
        showinfo(title='Help', message=showhelp)

    def filter():
        data = json.load(open('Exercise001/Notes.json'))
        inputstr = userdate.get('1.0', 'end')
        inputstr = inputstr[:9]
        flag = 0
        window.rowconfigure(index=1, weight=1)
        window.columnconfigure(index=1, weight=1)  
        columns = ('ID', 'Title', 'Note', 'Modified')
        tree = ttk.Treeview(columns=columns, show="headings")
        tree.place(height=400, width=950, x=20, y=20)
        tree.heading('ID', text='ID', anchor=CENTER)
        tree.heading('Title', text='Title', anchor=CENTER)
        tree.heading('Note', text='Note', anchor=CENTER)
        tree.heading('Modified', text='Modified', anchor=CENTER)
        tree.column("#1", stretch=NO, width=30, anchor=CENTER)
        tree.column("#2", stretch=NO, width=250, anchor=CENTER)
        tree.column("#3", stretch=YES, anchor=CENTER)
        tree.column("#4", stretch=NO, width=200, anchor=CENTER)
        for var in data:
            if inputstr in var[3]:
                tree.insert('', END, values=var)
                flag +=1
        if flag == 0:
            showinfo(message='Request not found!\nTry another date using format \nd/m/yyyy.')
        scrol_vert = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrol_vert.set)
        scrol_vert.place(width=5, x=970)

    def refresh():
        data = json.load(open('Exercise001/Notes.json'))
        window.title('List of stored notes')
        window.geometry('1000x550')
        window.rowconfigure(index=1, weight=1)
        window.columnconfigure(index=1, weight=1)  
        columns = ('ID', 'Title', 'Note', 'Modified')
        tree = ttk.Treeview(columns=columns, show="headings")
        tree.place(height=400, width=950, x=20, y=20)
        tree.heading('ID', text='ID', anchor=CENTER)
        tree.heading('Title', text='Title', anchor=CENTER)
        tree.heading('Note', text='Note', anchor=CENTER)
        tree.heading('Modified', text='Modified', anchor=CENTER)
        tree.column("#1", stretch=NO, width=30, anchor=CENTER)
        tree.column("#2", stretch=NO, width=250, anchor=CENTER)
        tree.column("#3", stretch=YES, anchor=CENTER)
        tree.column("#4", stretch=NO, width=200, anchor=CENTER)
        for var in data:
            tree.insert('', END, values=var)
        scrol_vert = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrol_vert.set)
        scrol_vert.place(width=5, x=970)

    window = Tk()
    data = json.load(open('Exercise001/Notes.json'))
    window.title(f'Hello, {name}!')
    window.geometry('1000x550')
    window.rowconfigure(index=1, weight=1)
    window.columnconfigure(index=1, weight=1)  
    columns = ('ID', 'Title', 'Note', 'Modified')
    tree = ttk.Treeview(columns=columns, show="headings")
    tree.place(height=400, width=950, x=20, y=20)
    tree.heading('ID', text='ID', anchor=CENTER)
    tree.heading('Title', text='Title', anchor=CENTER)
    tree.heading('Note', text='Note', anchor=CENTER)
    tree.heading('Modified', text='Modified', anchor=CENTER)
    tree.column("#1", stretch=NO, width=30, anchor=CENTER)
    tree.column("#2", stretch=NO, width=250, anchor=CENTER)
    tree.column("#3", stretch=YES, anchor=CENTER)
    tree.column("#4", stretch=NO, width=200, anchor=CENTER)
    for var in data:
        tree.insert('', END, values=var)
    scrol_vert = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrol_vert.set)
    scrol_vert.place(width=5, x=970)
    btn1 = Button(window, text='Filter by date', command=filter)
    btn2 = Button(window, text='New note', command=add)
    btn3 = Button(window, text='Editor', command=editor)
    btn4 = Button(window, text='Help', command=help)
    btn5 = Button(window, text='Refresh', command=refresh)
    btn6 = Button(window, text='Exit', command=exit)
    btn1.place(height=28, width=95, x=20, y=450)
    btn2.place(height=28, width=95, x=453, y=450)
    btn3.place(height=28, width=95, x=876, y=450)
    btn4.place(height=28, width=95, x=20, y=500)
    btn5.place(height=28, width=95, x=453, y=500)
    btn6.place(height=28, width=95, x=876, y=500)
    userdate = Text(window)
    userdate.place(height=28, width=95, x=120, y=450)
    mainloop()

main()