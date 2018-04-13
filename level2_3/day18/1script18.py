from tkinter import *
import tkinter.messagebox
import threading
import multiprocessing
import time
from runpy import run_path

data = []

def make_app():
    app = Tk()
    app.title('Script Operator')
    Button(name='add',text='Add',command=add_task).pack(side=BOTTOM)
    app.geometry('150x300')
    return app

def add_task():
    _font=['Arial',18,'bold']
    f = Frame(bg='#f2f2f2')
    #fm=Frame().pack() x can not use as this!!!!
    Label(f,name='script',text='script',font=_font,bg='#f2f2f2').pack(anchor=NW)
    Label(f,name='time',text='time',bg='#f2f2f2').pack(side=LEFT)
    Button(f,text='setting',command=lambda :setting_win(f)).pack(anchor=SE)
    f.pack(fill=X,padx=1,pady=1)

def setting_win(f):
    t = Toplevel(f)
    Label(t,text='File path:').grid(row=0,column=0,sticky=W)
    Entry(t,name='file_ipt').grid(row=1,column=0)
    Label(t,text='Start time:').grid(row=2,column=0,sticky=W)
    Entry(t,name='time_ipt').grid(row=3,column=0)
    Button(t,text='Save',command=lambda :(save(t),t.destroy())).grid(row=4,column=0)

def save(t):
    d = {}
    file_ipt = t.children['file_ipt'].get()
    time_ipt = t.children['time_ipt'].get()
    d['file_ipt'] = file_ipt
    d['time_ipt'] = time_ipt
    d['execute'] = False
    data.append(d)

def watcher():
    def _task_tag_update():
        tasks = [t[1] for t in app.children.items() if t[0] != 'add'] #tasks=each task Frame
        for d,t in zip(data,tasks):
            t.children['script']['text'] = d['file_ipt']
            t.children['time']['text'] = d['time_ipt']
            # t.children = task.children = lb-script & lb_time

    def _task_time_check():
        now = time.ctime().split()[-2]
        for d in data:
            if d['time_ipt'] <= now and not d['execute']:
                p = multiprocessing.Process(
                    target=lambda :run_path(d['file_ipt']))
                p.start()
                d['execute'] = True

    def _main():
        while True:
            time.sleep(0.5)
            _task_tag_update()
            _task_time_check()

    t = threading.Thread(target=_main)
    t.start()




app = make_app()
app.after(0,watcher)
app.mainloop()