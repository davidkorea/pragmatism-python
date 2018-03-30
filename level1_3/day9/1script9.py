from tkinter import *
import time
import psutil

# make_app -> speed_text -> ui_update

def make_app():
    app = Tk()
    app.geometry('300x150')
    app.config(bg='#303030')
    app.title('App')
    Label(text='Speed Monitor',
          font=('Arial',25,'bold'),
          bg='#303030',
          fg='white',
          pady=15
          ).pack()
    Label(name='l2',
          text='_kb/s',
          font=('Arial',25,'bold'),
          bg='#303030',
          fg='white',
          pady=5
          ).pack()
    return app

def speed_test():
    t1 = psutil.net_io_counters(pernic=True)['en0']
    time.sleep(1)
    t2 = psutil.net_io_counters(pernic=True)['en0']
    byte = t2.bytes_recv - t1.bytes_recv
    kbs = byte/1024
    return str(kbs)+'kb/s'

def ui_update(do):
    speed = do()
    l2 = app.children['l2']
    l2.config(text=speed)
    app.after(1000,lambda:ui_update(do))


app = make_app()
app.after(1000, lambda: ui_update(speed_test))

app.mainloop()