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


def add():
    window2 = Tk()
    window2.title('Edditing')
    window2.geometry('500x350')
    window2.rowconfigure(index=1, weight=1)
    window2.columnconfigure(index=1, weight=1)
    interList = []
    data = json.load(open('Notes.json'))
    id = len(data) + 1
    lbl_1 = Label(window2, text=f'New note ID: {id}')
    lbl_1.place(x=20, y=20)
    lbl_2 = Label(window2, text='Enter new Title:')
    editor2 = Text(window2, wrap=WORD)
    lbl_2.place(x=20, y=60)
    editor2.place(height=30, width=460, x=20, y = 85)
    lbl_3 = Label(window2, text='Enter new Note:')
    editor3 = Text(window2, wrap=WORD)
    lbl_3.place(x=20, y=120)
    editor3.place(height=150, width=460, x=20, y=145)
    def myprint():
        # window = Tk()
        # window.title(f'Hello!')
        data = json.load(open('Notes.json'))
        date_time = datetime.now()
        currentdate = f'{date_time.day}/{date_time.month}/{date_time.year} {date_time.hour}:{date_time.minute}:{date_time.second}'
        interList.append(id)
        interList.append(editor2.get("1.0", "end"))
        interList.append(editor3.get("1.0", "end"))
        interList.append(currentdate)
        data.append(interList)
        with open('Notes.json', 'w') as outfile:
                json.dump(data, outfile)
        outfile.close()
        showinfo(title='Add new note', message=f'Note ID #{id} has been successfully saved!\nClose edditing window to finish.')
        data = json.load(open('Notes.json'))    
    btn_1 = Button(window2, text='Save', command=myprint)
    btn_1.place(relx=0.43, y=300)