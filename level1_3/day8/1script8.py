# ui
# ui_update
# business

from tkinter import *
from PIL import Image as Img
from tkinter.filedialog import *
import getpass
import os

info = {
    'path':[]
}

def make_app():
    app = Tk()
    Label(app,text='Image Compress Tool',font=('Arial',25,'bold')).pack()
    Listbox(app,name='lbox',bg='#f2f2f2',fg='blue').pack(fill=BOTH,expand=True)
    Button(app,text='open',command=ui_get_data).pack()
    Button(app,text='compress',command=compress).pack()
    app.geometry('300x400')
    return app

def ui_get_data():
    file_names = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = file_names
    if info['path']:
        for name in file_names:
            lbox.insert(END, name.split('/')[-1])

def compress():
    for f_path in info['path']:
        login_user = getpass.getuser()
        # 其他电脑运行时，需要获取当前电脑登录名
        output = '/users/'+login_user+'/desktop/output/'
        if os.path.exists(output):
            name = f_path.split('/')[-1]
            image = Img.open(f_path)
            image.save(output+'c_'+name,quality=40)
        else:
            os.makedirs(output)
            name = f_path.split('/')[-1]
            image = Img.open(f_path)
            image.save(output + 'c_' + name, quality=40)


app=make_app()
app.mainloop()
