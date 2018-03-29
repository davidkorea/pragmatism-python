# coding:utf-8

'''
 make_app
 ui_get_data
 resize
'''

from tkinter import *
from tkinter.filedialog import *
from PIL import Image as Img
import getpass

size_list = [50,100,200,512]
info = {
    'path':[]
}

def make_app():
    app = Tk()
    Label(app,text='Image Resize Tool',font=('Arial',25,'bold')).pack()
    Listbox(app,name='lbox',bg='#f2f2f2').pack(fill=BOTH,expand=True)
    Button(app,text='open',command=ui_get_data).pack()
    Button(app,text='resize',command=resize_pic).pack()
    app.geometry('300x400')
    return app
def ui_get_data():
    images = askopenfilenames()
    lbox = app.children['lbox']
    info['path']= images
    for i in images:
        lbox.insert(END, i.split('/')[-1])

def resize_pic():
    for f_path in info['path']:
        output = '/users/osx/desktop/output/'
        name = f_path.split('/')[-1]
        image = Img.open(f_path)
        for s in size_list:
            image.resize((s,s)).save(output+str(s)+"_thumb_"+name)



app = make_app()
app.mainloop()