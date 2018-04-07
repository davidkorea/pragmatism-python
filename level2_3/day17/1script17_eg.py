# Core --> Core&UI --> Core&UI&User --> Boundary.Edge.Corner
# app app2
#  ||  \\

import time
from tkinter import *
from multiprocessing import Process
import threading

info = {
    'total_time':60
}

def make_app():
    _font = ['Hack',25,'bold']
    app = Tk()
    Label(name='lb',text=0,font=_font).pack()
    Button(name='btn',text='start',command=time_counts).pack()
    Entry(name='ipt').pack()
    app.geometry('150x75')
    return app

def time_counts():
    def _counts():
        while info['total_time']:
            info['total_time'] -= 1
            print(info['total_time'])
            time.sleep(1)

    t = threading.Thread(target=_counts,name='timer')
    t.start()

def ui_watcher():

    def _update_button():
        btn = app.children['btn']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if timer:
            btn['state'] = 'disabled' # 'disabled'
        else:
            btn['state'] = 'normal'

    def _get_time():
        ipt = app.children['ipt']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if not timer and ipt.get():
            info['total_time'] = int(ipt.get())

    def _update_time():
        lb = app.children['lb']
        lb['text'] = info['total_time']

    def _main():
        while True:
            #_update_button()
            print("I'm watching you")
            print(threading.enumerate())
            _get_time()
            _update_time()
            _update_button()
            time.sleep(0.5)

    t = threading.Thread(target=_main,name='watcher')
    t.start()

# 注意，在windows系统下，必须按此方法执行。linux/mac系统可以不要if这句话。
if __name__ == '__main__':
    app = make_app()
    #app.after(0,time_counts)
    app.after(0,ui_watcher)
    app.mainloop()