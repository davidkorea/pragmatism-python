from tkinter import *
import multiprocessing
import threading
import time
from runpy import run_path
import tkinter.messagebox
from tkinter.messagebox import Message

# make_app -> add_task -> setting -> ui_update -> run_path

data = []

def make_app():
    app = Tk()
    app.geometry('200x300')
    Button(app,text='Add',name='add',command=add_task).pack(side=BOTTOM)
    return app

def add_task():
    f = Frame(app,bg='#f2f2f2')
    Label(f,name='task_file',text='script',bg='#f2f2f2').pack(anchor=NW)
    Label(f,name='task_time',text='00:00',bg='#f2f2f2').pack(side=LEFT)
    Button(f,name='setting',text='...',width=3,command=lambda :setting(f)).pack(side=RIGHT)
    f.pack(fill=X,padx=1,pady=1)

def setting(f):
    t = Toplevel(f)
    v = StringVar(t,value='12:00')
    Label(t,name='file_path',text='File path').grid(row=0,column=0,sticky=W)
    Entry(t,name='path_ipt').grid(row=1,column=0)
    Button(t,name='find_path',text='...',width=3,command=lambda :find_path(t)).grid(row=1,column=1)
    Label(t,name='time',text='Time').grid(row=2,column=0,stick=W)
    Entry(t,name='time_ipt',textvariable=v).grid(row=3,column=0)
    Button(t,name='save',text='Save',command=lambda :(
                                                        save(t),
                                                        t.destroy()
                                                    )
           ).grid(row=4,column=0,columnspan=2)

def find_path(t):
    path = askopenfilename()
    file_name = path.split('/')[-1]
    v=StringVar(value=file_name)
    t.children['path_ipt']['textvariable'] = v

def save(t):
    d = {}
    path_ipt = t.children['path_ipt'].get()
    time_ipt = t.children['time_ipt'].get()
    d['path_ipt'] = path_ipt
    d['time_ipt'] = time_ipt
    d['execute'] = False
    d['data_exsit'] = False
    data.append(d)
    print(data)

def ui_update():
    def _task_update():
        # f['task_file']=data['path_ipt']
        # f['task_time']=data['time_ipt']
        # app.task_Frame -> Frame.Label = f['task_file']
        # app.children.items() = all task frames + Add button
        tasks = [t[1] for t in app.children.items() if t[0] != 'add']
        for t,d in zip(tasks,data):
            t.children['task_file']['text'] = d['path_ipt']
            t.children['task_time']['text'] = d['time_ipt']


    def _restrict():
        # tasks = [t[1] for t in app.children.items() if t[0] != 'add']
        # for t in tasks:
        #     if t.children['task_file'] == None:
            # if d['path_ipt'] and not d['data_exsit']:
        # for d in data:
        #     if not d['path_ipt'] and not d['data_exsit']:
        #         tkinter.messagebox.showerror('ERR','Setting first')
        #         d['data_exsit'] = True

        pass

    def _task_time_check():
        now = time.ctime().split()[-2]
        for d in data:
            if d['time_ipt'] <= now and not d['execute']:
                p = multiprocessing.Process(target=lambda :run_path(d['path_ipt']))
                p.start()
                d['execute'] = True

    def _main():
        while True:
            time.sleep(0.5)
            _task_update()
            _task_time_check()
            _restrict()

    t = threading.Thread(target=_main)
    t.start()





app = make_app()
app.after(0,ui_update)
app.mainloop()