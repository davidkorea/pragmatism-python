# coding:utf-8
from tkinter import *
from tkinter.filedialog import *
from PIL import Image as Img

# 将指定的像素大小存到list变量中
size_list = [50, 100, 120, 180, 512]
info = {
    'path':[]
}

# 创建一个GUI框体
def make_app():
    app = Tk()
    Label(app, text='Image compress tool', font=('Hack',20,'bold')).pack()
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app, text='open', command=ui_getdata).pack()
    Button(app, text='resize', command=resize_pic).pack()
    app.geometry('300x400')
    return app
# 获取文件，并将其展示在listbox组件中
def ui_getdata():
    f_names = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = f_names
    if info['path']:
        for name in f_names:
            lbox.insert(END, name.split('/')[-1])
# 利用resize函数，修改图像大小
def resize_pic():
    for f_path in info['path']:
        output = '/users/osx/desktop/output/'
        name = f_path.split('/')[-1]
        image = Img.open(f_path)
        for s in size_list:
            image.resize((s,s)).save(output+str(s)+"_"+name)

# 调用函数生成框体
app = make_app()
app.mainloop()
