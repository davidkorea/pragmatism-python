from tkinter import *
import time
import threading
info = {
    'total_time':60
}

def make_app():
    app = Tk()
    _font = ['Arial',25,'bold']
    Label(name='lb',text=0,font=_font).pack()
    Entry(name='input').pack()
    Button(name='btn1',text='Start',command=start_count)
    Button(name='btn2',text='Stop',command=stop_count)
    app.geometry('150x100')
    app.title('Watch')
    return app


def start_count():
    def _count():
        while info['total_time']:
            info['total_time'] -= 1
            time.sleep(1)
            print(info['total_time'])
    t = threading.Thread(target=_count,name='count')
    t.start()

def stop_count():
    info['total_time'] = 0

def ui_update():
    def _button_update():
        btn1 = app.children['btn1']
        btn2 = app.children['btn2']
        count = [c for c in threading.enumerate() if c.name == 'count']
        if count:
            # btn1['state']='disable'
            btn2.pack()
            btn1.pack_forget()
        else:
            # btn1['state']='normal'
            btn1.pack()
            btn2.pack_forget()

    def _entry_update():
        input = app.children['input']
        count = [c for c in threading.enumerate() if c.name == 'count']
        if count:
            input['state']='disable'
        else:
            input['state']='normal'


    def _input_time():
        input = app.children['input']
        count = [c for c in threading.enumerate() if c.name == 'count']
        if not count and input.get():
            info['total_time'] = int(input.get())

    def _count_update():
        lb = app.children['lb']
        lb['text'] = info['total_time']

    def _main():
        while True:
            _count_update()
            _input_time()
            _button_update()
            _entry_update()

    t = threading.Thread(target=_main)
    t.start()




app = make_app()
app.after(0,ui_update)
app.mainloop()