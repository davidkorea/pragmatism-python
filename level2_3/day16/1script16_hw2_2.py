'''
① 在课程代码基础上增加一个 open 按钮，能弹出系统弹窗选择任意路径的文件，
然后将文件移动到这个项目代码所在的 GUI 文件目录列表中，
并且在程序界面的 listbox 中显示了这个文件。
② 当某个程序运行结束的时候，在界面上这个任务的这一行显示 √
'''
from tkinter import *
from tkinter.filedialog import *
from runpy import run_path
import multiprocessing
import threading
import time

file_path = []

def make_app():
    app = Tk()
    Listbox(name='lbox').pack()
    Button(name='open',text='open',command=open_path).pack()
    Button(name='run',text='run',command=run).pack()
    return app

def open_path():
    files = askopenfilenames()
    lbox = app.children['lbox']
    data = {}
    for f in files:
        show_name = f.split('/')[-1]
        lbox.insert(END,show_name)
        data['name'] = show_name
        data['path'] = f
        data['status'] = False
        file_path.append(data)
        print(data)
        
# 打开几个文件路径，就会有几个相同process运行，不知道是为什么...??
# 同时运行，stop可以同时结束
# ******* fixed ********
#  askopenfilenames（）
#  when use mouse or shift select multi files
#  the file_path list will add the same path which is the last file of these files
#  kinda the bug of askopenfilenames()
#  if you select file one by one, the file_path would add each file's correct path
# **********************

# 其它路径的文件已经可以正常运行

def run():
    lbox = app.children['lbox']
    actv_file = lbox.get(ACTIVE) #show_name
    # print(actv_file)
    for sub in file_path:
        # print(sub)
        if sub['name'] == actv_file:
            print(sub['path'])
            p = multiprocessing.Process(name=sub['name'],
                                        target=lambda :run_path(sub['path']))
            p.start()
            # if multiprocessing.current_process().exitcode == sub['name']


def stop():
    lbox = app.children['lbox']
    actv_file = lbox.get(ACTIVE)  # show_name
    for p in multiprocessing.active_children():
        if p.name == actv_file:
            p.terminate()



def ui_update_watcher():
    def _btn_stop():
        if multiprocessing.active_children():
            app.children['run']['text'] = 'stop'
            app.children['run']['command'] = stop
        else:
            app.children['run']['text'] = 'run'
            app.children['run']['command'] = run

    def _tsk_update():
        print(file_path)
        print(multiprocessing.active_children())
        # for p in multiprocessing.active_children():
        #     if p.name:
        lbox = app.children['lbox']
        actv_file = lbox.get(ACTIVE)
        print(actv_file + ' is ACTIVE')


    def _main():
        while True:
            time.sleep(0.5)
            _btn_stop()
            _tsk_update()

    t = threading.Thread(target=_main)
    t.start()

app = make_app()
app.after(0,ui_update_watcher)
app.mainloop()
