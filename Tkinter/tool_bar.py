from tkinter import *

def nothing():
    print('ok,ok,won`t')

root = Tk()
# ***** Menu *****
menu=Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='File',menu=subMenu)
subMenu.add_command(label='New Project...',command=nothing)
subMenu.add_command(label='New...',command=nothing)
subMenu.add_separator()
subMenu.add_command(label='Exit',command=nothing)

editMenu = Menu(menu)
menu.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Redo',command=nothing)

# ***** Toolbar *****
# Frame should be pack() at the very last

toolBar = Frame(root,bg='#f2f2f2')
openButt = Button(toolBar,text='open',command=nothing).pack(side=LEFT,padx=2)
instButt = Button(toolBar,text='insert',command=nothing).pack(side=LEFT,padx=2)
toolBar.pack(side=TOP, fill=X)

root.mainloop()