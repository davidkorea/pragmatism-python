from tkinter import *
# ONly? grid could put button in the frame??? pack() doesnt work??
app = Tk()
fm = Frame(app,bg='red').grid(row=0,column=0)
btn = Button(fm,text='1234').grid(row=0,column=0,sticky=NW)

app.mainloop()
