import csv
from tkinter import *
form = Tk()
form.title('CSV Parsing')
form.geometry('290x100')
form.resizable(0, 0)
form.config(bg='#00c4ff')
with open('test.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    r=0
    for column in reader:
        c=0
        for row in column:
            if r==0:
                label01 = Label(form, text=row,bg='#00c4ff',
                relief=RIDGE,width=10,font='Arial 15 bold')
            else:
                label01 = Label(form, text=row,bg='#8ec06c',
                relief=RIDGE,width=10)
            label01.grid(row=r,column=c,sticky='NSEW')
            c=c+1
        r=r+1
csvFile.close()
form.mainloop()

