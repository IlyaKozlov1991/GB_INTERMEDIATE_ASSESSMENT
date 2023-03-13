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

data = json.load(open('Notes.json'))

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

    def editor():
        def edit():
            def editID():
                var = int(entry1.get())
                data = json.load(open('Notes.json'))
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
                                    data = json.load(open('Notes.json'))
                                    date_time = datetime.now()
                                    currentdate = f'{date_time.day}/{date_time.month}/{date_time.year} {date_time.hour}:{date_time.minute}:{date_time.second}'
                                    data[i][1] = newtitle.get('1.0', 'end')
                                    data[i][2] = newnote.get('1.0', 'end')
                                    data[i][3] = currentdate
                                    with open('Notes.json', 'w') as outfile:
                                        json.dump(data, outfile)
                                    outfile.close()
                                    showinfo(title='Add new note', message=f'Note ID #{var} has been successfully changed!\nClose edditing window to finish.')
                                    data = json.load(open('Notes.json'))
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
                    data = json.load(open('Notes.json'))
                    for val in data:
                        for i in range(len(val)):
                            if val[i] == var:
                                data.remove(val)
                                with open('Notes.json', 'w') as outfile:
                                    json.dump(data, outfile)
                                outfile.close()
                                showinfo(title='Add new note', message=f'Note ID #{var} has been deleted!\nClose edditing window to finish.')
                                data = json.load(open('Notes.json'))
                else:
                    showinfo(title='Abort', message='Operation aborted')   
            lbl_1.configure(text='Enter ID of note to be removed:')
            entry1 = Entry(window3)
            entry1.place(height=30, width=50, x=187, y=50)
            btn_1.configure(command=removeID)
            btn_2.configure(text='Cancel', command=exit)
        window3 = Tk()
        data = json.load(open('Notes.json'))
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
            window.title(f'Hello, {name}!')
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

    def filter():
        data = json.load(open('Notes.json'))
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
            showinfo(message='Request not found!\nTry another date.')
        scrol_vert = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrol_vert.set)
        scrol_vert.place(width=5, x=970)

    def refresh():
        data = json.load(open('Notes.json'))
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
    data = json.load(open('Notes.json'))
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