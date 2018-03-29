from tkinter.filedialog import *
from PIL import Image as Img
import tkinter

info = {
    'path':[]
}
output = {
    'path':[]
}

def make_app():
    app = Tk()
    Label(app,text='Thumb Tool',font=('Arial',25,'bold')).pack()
    Listbox(app,name='lbox',bg='#f2f2f2').pack(fill=BOTH,expand=True)
    Button(app,text='open files',command=ui_open_files).pack()
    Listbox(app,name='out_lbox',bg='#f2f2f2').pack(fill=BOTH,expand=True)
    Button(app,text='output path',command=ui_out_path).pack()
    Button(app,text='resize',command=resize_pic).pack()
    app.geometry('300x600')
    return app

def ui_open_files():
    image_open = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = image_open
    for i in image_open:
        lbox.insert(END,i)
        # i.split('/)[-1] shows no path, only file name

def ui_out_path():
    output_select = askdirectory()
    # output = print(output_open)
    out_lbox = app.children['out_lbox']
    out_lbox.insert(END,output_select)
    output['path'] = output_select
    print(output['path'])

def resize_pic():
    for path in info['path']:
        size_list = [80,160]
        name = path.split('/')[-1]
        image = Img.open(path)
        for s in size_list:
            image.resize((s,s)).save(output['path']+"/th_"+str(s)+name)

app = make_app()
app.mainloop()
