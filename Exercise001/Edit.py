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

def editor():
        print('Editor')
        def edit():
            def editID():
                var = int(entry1.get())
                data = json.load(open('Exercise001/Notes.json'))
                for i in range(len(data)):
                        for j in range(len(data[i])):
                            if data[i][j] == var:
                                editwindow = Tk()
                                editwindow.title(f'Edditing of the note ID #{var}')
                                editwindow.geometry('500x350')
                                editlbl1 = Label(editwindow, text='Enter new Title:')
                                editlbl1.place(x=20, y=20)
                                newtitle = Text(editwindow, wrap=WORD)
                                newtitle.place(height=30, width=460, x=20, y = 45)
                                editlbl2 = Label(editwindow, text='Enter new Note:')
                                editlbl2.place(x=20, y=75)
                                newnote = Text(editwindow, wrap=WORD)
                                newnote.place(height=150, width=460, x=20, y=105)
                                def writenew():
                                    data = json.load(open('Exercise001/Notes.json'))
                                    date_time = datetime.now()
                                    currentdate = f'{date_time.day}/{date_time.month}/{date_time.year} {date_time.hour}:{date_time.minute}:{date_time.second}'
                                    data[i][1] = newtitle.get('1.0', 'end')
                                    data[i][2] = newnote.get('1.0', 'end')
                                    data[i][3] = currentdate
                                    with open('Exercise001/Notes.json', 'w') as outfile:
                                        json.dump(data, outfile)
                                    outfile.close()
                                    showinfo(title='Add new note', message=f'Note ID #{var} has been successfully changed!\nClose edditing window to finish.')
                                    data = json.load(open('Exercise001/Notes.json'))
                                btn_1 = Button(editwindow, text='Save', command=writenew)
                                btn_1.place(height=28, width=95, x=203, y=300)
            lbl_1.configure(text='Enter ID of note to be modified:')
            entry1 = Entry(window3)
            entry1.place(height=30, width=50, x=187, y=50)
            btn_1.configure(text='Edit', command=editID)
            btn_2.configure(text='Cancel', command=exit)
        def remove():
            def removeID():
                var = int(entry1.get())
                askuser = askyesno(title='Confirm operation', message='Are you sure to delete note?')
                if askuser:
                    data = json.load(open('Exercise001/Notes.json'))
                    for val in data:
                        for i in range(len(val)):
                            if val[i] == var:
                                data.remove(val)
                                with open('Exercise001/Notes.json', 'w') as outfile:
                                    json.dump(data, outfile)
                                outfile.close()
                                showinfo(title='Add new note', message=f'Note ID #{var} has been deleted!\nClose edditing window to finish.')
                                data = json.load(open('Exercise001/Notes.json'))
                else:
                    showinfo(title='Abort', message='Operation aborted')   
            lbl_1.configure(text='Enter ID of note to be removed:')
            entry1 = Entry(window3)
            entry1.place(height=30, width=50, x=187, y=50)
            btn_1.configure(command=removeID)
            btn_2.configure(text='Cancel', command=exit)
        window3 = Tk()
        data = json.load(open('Exercise001/Notes.json'))
        window3.title('Edditing')
        window3.geometry('425x150')
        window3.rowconfigure(index=1, weight=1)
        window3.columnconfigure(index=1, weight=1)
        lbl_1 = Label(window3, text='Remove -> delete specified note\nEdit -> change specified note') 
        lbl_1.place(relx=0.27, y=20)
        btn_1 = Button(window3, text='Remove', command=remove)
        btn_1.place(height=28, width=95, x=20, y=100)
        btn_2 = Button(window3, text='Edit', command=edit)
        btn_2.place(height=28, width=95, x=310, y=100)