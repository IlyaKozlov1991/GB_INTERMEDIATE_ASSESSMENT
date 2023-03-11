# GeekBrains intermediate assessment Exercise001
# Create a notes app

import os
import json
from datetime import date
from datetime import time
from datetime import datetime
from tabulate import tabulate
import easygui
from easygui import *

data = json.load(open('Notes.json'))

id = 0

name = os.environ.get('USER')

print(f'Hello, {name}!')

command = ''

def all_notes(list, dict):
    inner_list1 = []
    inner_list2 = []
    inner_list3 = [['ID', 'Title', 'Note', 'Modified']]
    for i in range(len(list)):
        inner_list1.append(list[i])
        inner_list1.append(dict[list[i]]['Title'])
        inner_list1.append(dict[list[i]]['Body'])
        inner_list1.append(dict[list[i]]['Date'])
    def cut_list(list1, list2, list3):
            for i in range(len(list3[0])):
                list1.append(list2[0])
                list2.pop(0)
    k = 1
    # while k <= len(inner_list1) + 1:
    while len(inner_list1) != 0:
        cut_list(inner_list2, inner_list1, inner_list3)
        inner_list3.append(inner_list2)
        inner_list2 = []
        k += 1
    return inner_list3

def main():
    data = json.load(open('Notes.json'))

    id = 0
    
    global choise1
    choise1 = ''
    while choise1 != 'Exit':
        choises1 = ['Show notes', 'New note', 'Exit']
        choise1 = (buttonbox('Show notes - print list of all notes\nNew note - add a new note\nExit - close program', f'Hello, {name}!', choises1))
        if choise1 == 'Show notes':
            data = json.load(open('Notes.json'))
            mainList = []
            for var in data.keys():
                mainList.append(var)
            choises2 = ['Filter by date', 'Edit', 'Remove', 'Home']
            output = indexbox(tabulate(all_notes(mainList, data)), 'Press to continue', choises2)
            while output != 3: # 0 -> Filter by date | 1 -> Edit | 2 -> Remove | 3 -> Back
                if output == 1:
                        id = enterbox('Enter Note ID: ')
                        title = enterbox('Enter Title: ')
                        body = enterbox('Enter Note: ')
                        date_time = datetime.now()
                        currentdate = f'{date_time.day}/{date_time.month}/{date_time.year} {date_time.hour}:{date_time.minute}:{date_time.second}'
                        data[id] = {'Title': title, 'Body': body, 'Date': currentdate}
                        with open('Notes.json', 'w') as outfile:
                            json.dump(data, outfile)
                            outfile.close()
                        data = json.load(open('Notes.json'))
                        editbox = msgbox(f'Note ID {id} successfully updated!')
                        if editbox == 'OK':
                            break
                elif output == 0:
                    def filter():
                            userDate = enterbox('Enter your date in format d/m/yyyy: ')
                            mylist = []
                            for var in data.keys():
                                mylist.append(var)
                            interdict = {}
                            for i in range(len(data)):
                                if userDate in data[mylist[i]]['Date']:
                                    interdict[mylist[i]] = data[mylist[i]]
                                    i += 1
                                else:
                                    i += 1
                            mylist2 = []
                            for var in interdict.keys():
                                mylist2.append(var)
                            return tabulate(all_notes(mylist2, interdict))
                            # msgbox(tabulate(all_notes(mylist2, interdict)))
                    choises3 = ['New filter', 'Home']
                    filterbox = ccbox(filter(), 'List of notes', choises3)
                    while filterbox != False: # True -> New filter | False -> Home
                        filterbox = ccbox(filter(), 'List of notes', choises3)
                    else:
                        break
                elif output == 2:
                    userInput = enterbox('Enter ID of note to be removed:')
                    data.pop(userInput)
                    with open('Notes.json', 'w') as outfile:
                        json.dump(data, outfile)
                        outfile.close()
                    data = json.load(open('Notes.json'))
                    removebox = msgbox(f'Note ID {userInput} has been removed!')
                    if removebox == 'OK':
                        break
        elif choise1 == 'New note':
            id = len(data) + 1
            title = enterbox('Enter Title: ')
            body = enterbox('Enter Note: ')
            date_time = datetime.now()
            currentdate = f'{date_time.day}/{date_time.month}/{date_time.year} {date_time.hour}:{date_time.minute}:{date_time.second}'
            data[id] = {'Title': title, 'Body': body, 'Date': currentdate}
            with open('Notes.json', 'w') as outfile:
                json.dump(data, outfile)
            outfile.close()
            data = json.load(open('Notes.json'))           

main()