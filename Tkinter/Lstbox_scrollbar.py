from tkinter import *

app = Tk()
fm = Frame(name='fm',bg='#f2f2f2')
Listbox(fm,name='lbox').pack(side=LEFT)
for i in range(100):
    app.children['fm'].children['lbox'].insert(END,i)

Scrollbar(fm,name='sbar').pack(side=RIGHT,fill=Y)
app.children['fm'].children['lbox']['yscrollcommand'] = app.children['fm'].children['sbar'].set
app.children['fm'].children['sbar']['command'] = app.children['fm'].children['lbox'].yview
fm.pack()
Button(text='Add').pack(side=BOTTOM)
app.mainloop()