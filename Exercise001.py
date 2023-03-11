# GeekBrains intermediate assessment Exercise001
# Create a notes app

import os
import json
from datetime import date
from datetime import time
from datetime import datetime
from tabulate import tabulate

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

while command != 'exit':
    command = str(input('Enter your command: '))
    if command == 'print':
        data = json.load(open('Notes.json'))
        mainList = []
        for var in data.keys():
            mainList.append(var)
        print(tabulate(all_notes(mainList, data), headers='firstrow', tablefmt='fancy_grid', stralign='left'))
    elif command == 'add':
        id = len(data) + 1
        title = str(input('Enter Title: '))
        body = str(input('Enter Note: '))
        date_time = datetime.now()
        currentdate = f'{date_time.day}/{date_time.month}/{date_time.year} {date_time.hour}:{date_time.minute}:{date_time.second}'
        data[id] = {'Title': title, 'Body': body, 'Date': currentdate}
        with open('Notes.json', 'w') as outfile:
            json.dump(data, outfile)
            outfile.close()
        data = json.load(open('Notes.json'))
    elif command == 'edit':
        id = str(input('Enter Note ID: '))
        title = str(input('Enter Title: '))
        body = str(input('Enter Note: '))
        date_time = datetime.now()
        currentdate = f'{date_time.day}/{date_time.month}/{date_time.year} {date_time.hour}:{date_time.minute}:{date_time.second}'
        data[id] = {'Title': title, 'Body': body, 'Date': currentdate}
        with open('Notes.json', 'w') as outfile:
            json.dump(data, outfile)
            outfile.close()
        data = json.load(open('Notes.json'))

a = '12/3/2023'

mylist = []
for var in data.keys():
    mylist.append(var)

interdict = {}

for i in range(len(data)):
    if a in data[mylist[i]]['Date']:
        interdict[mylist[i]] = data[mylist[i]]
        i += 1
    else:
        i += 1

mylist2 = []
for var in interdict.keys():
    mylist2.append(var)

print(tabulate(all_notes(mylist2, interdict), headers='firstrow', tablefmt='fancy_grid', stralign='left'))