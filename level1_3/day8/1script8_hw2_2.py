# Tkinter grid reference: http://www.cnblogs.com/ruo-li-suo-yi/p/7425307.html

from PIL import Image as Img
from tkinter.filedialog import *
# import tkinter

info = []

def make_app():
    # app = Tk()
    Label(app,text='Image Resize tool',font=('Arial',25,'bold')).grid(row=0,columnspan=3)
    Listbox(app,name='lbox',bg='#f2f2f2').grid(row=1,columnspan=3)
    Label(app,text='Select images').grid(row=2,column=0,sticky=W)
    Button(app,text='open',command=ui_select_pic).grid(row=2,column=2,columnspan=2,sticky=W,padx=5)
    Label(app,text='Output path').grid(row=3,column=0,sticky=W)
    Entry(app,textvariable=show_path).grid(row=3,column=1)
    Button(app,text='find',command=ui_output_path).grid(row=3,column=2,sticky=W,padx=5)
    Label(app,text='Resize').grid(row=4,column=0,sticky=W)
    Button(app,text='resize',command=resize).grid(row=4,column=2,columnspan=2,sticky=W,padx=5)
    app.geometry('340x300')
    app.title('App')
    # return app

def ui_select_pic():
    select_pic = askopenfilenames()
    for pic in select_pic:
        pic_name = pic.split('/')[-1]
        app.children['lbox'].insert(END,pic_name)
        info.append(pic)
    # print(info)

def ui_output_path():
    select_path = askdirectory()
    show_path.set(select_path)

def resize():
    size = [60,120]
    for pic in info:
        output = show_path.get()
        name = pic.split('/')[-1]
        image = Img.open(pic)
        for s in size:
            image.resize((s,s)).save(output+'/cut_'+str(s)+name)

app = Tk()
show_path = StringVar() #不知道为什么 必须在这个位置 其他位置报错
make_app()
app.mainloop()