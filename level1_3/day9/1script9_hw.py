from tkinter import *
import time
import keyboard

# make_app -> type_in -> ui_update

def make_app():
    app = Tk()
    app.geometry('300x150')
    app.title('App')
    app.config(bg='#303030')
    Label(text='Type in Speed',
          bg='#303030',
          fg='white',
          pady=15,
          font=('Arial',25,'bold')
          ).pack()
    Label(name='lb2',
          text='_letter/sec',
          bg='#303030',
          fg='white',
          pady=10,
          font=('Arial', 25, 'bold')
          ).pack()
    return app

def type_in():
    keyboard.start_recording()
    # tst = random.randrange(2,20)
    time.sleep(1)
    s = keyboard.stop_recording()
    speed = len(s)//2
    return str(speed)+' letters/sec'

def ui_dpdate(do):
    speed = do()
    lb2 = app.children['lb2']
    lb2.config(text=speed)
    app.after(1000,lambda: ui_dpdate(do))

app = make_app()
app.after(1000,lambda: ui_dpdate(type_in))
app.mainloop()