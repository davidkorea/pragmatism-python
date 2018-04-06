from tkinter import *
from tkinter.filedialog import *
import multiprocessing
import os
from runpy import run_path


file_path = []

def make_app():
    app = Tk()
    app.title('App')
    Listbox(name='lbox').pack()
    Button(text='Open',command=select_files).pack()
    Button(text='Run',command=run_script).pack()
    Button(text='Stop',command=stop_script).pack()
    return app

def select_files():
    lbox = app.children['lbox']
    files = askopenfilenames()
    for f in files:
        show_name = f.split('/')[-1]
        lbox.insert(END,show_name)
        file_path.append(f)
    print(file_path)

def run_script():
    lbox = app.children['lbox']
    active_file = lbox.get(ACTIVE)
    for child in multiprocessing.active_children():
        if child.name == active_file:
            print('Already started')
            return
    p = multiprocessing.Process(name=active_file,target=lambda : run_path(active_file))
    p.start()


def stop_script():
    lbox = app.children['lbox']
    active_file = lbox.get(ACTIVE)
    for p in multiprocessing.active_children():
        if p.name == active_file:
            p.terminate()


def watch_dog():
    for p in multiprocessing.active_children():
        print('RUnning Process: '+p.name)
    lbox = app.children['lbox']
    active_file = lbox.get(ACTIVE)
    if active_file:
        print(active_file+' is ACTIVE')
    app.after(1000,watch_dog)


app = make_app()
app.after(0,watch_dog)
app.mainloop()
