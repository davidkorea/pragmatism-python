from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo('Info','Just an info window')
tkinter.messagebox.showerror('Err','016-555')
quiz = tkinter.messagebox.askquestion('Quiz','whats your name')
if quiz == 'yes':
    print('Thx')
else:
    print('no')

root.mainloop()