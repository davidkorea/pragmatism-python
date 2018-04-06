from runpy import run_path
from tkinter import *
import multiprocessing
import os

def make_app():
    app = Tk()
    app.title('Run Script')
    Listbox(name='lbox').pack()
    Button(text='Run',name='run', command=run_script).pack()
    Button(text='Stop',name='stop',command=stop_script).pack()
    return app

def run_script():
    lbox = app.children['lbox']
    s_path = lbox.get(ACTIVE)
    for child in multiprocessing.active_children():
        if  child.name == s_path:
            print('already running')
            return
        # can ot use IF-ELSE ??dono why
    p = multiprocessing.Process(name=s_path, target=lambda: run_path(s_path))
    p.start()


    # run_path('testcode.py')


def stop_script():
    lbox = app.children['lbox']
    s_path = lbox.get(ACTIVE)
    for p in multiprocessing.active_children():
        if p.name == s_path:
            p.terminate()

def ui_update():
    lbox = app.children['lbox']
    files = os.listdir('./')
    for f in files:
        if not f.startswith('.'):
            lbox.insert(END,f)

def watch_dog():
    print(multiprocessing.active_children())
    lbox = app.children['lbox']
    s_path = lbox.get(ACTIVE)
    print(s_path+' is ACTIVE')
    app.after(1000,watch_dog)


app = make_app()
app.after(100,ui_update) # OR else listbox will show nothing
app.after(1,watch_dog)
app.mainloop()