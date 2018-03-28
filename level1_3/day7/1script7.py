import os
from tkinter import *

app = Tk()
label =Label(text='All Hidden Files', font=('Hack',25,'bold'))
label.pack()
listbox = Listbox(bg='#f2f2f2',fg='red')
listbox.pack(fill=BOTH,expand=True)
path = '/Users/osx/'
files = os.listdir(path)
for f in files:
    if f.startswith('.'):
        listbox.insert(END,f)
app.mainloop()