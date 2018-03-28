from tkinter import *
import pip

app = Tk()
label = Label(text="Installed Packages",font=('Hack',25,'bold'))
label.pack()
listbox = Listbox(bg='#f2f2f2',fg='blue',font=('',20,''))
listbox.pack(fill=BOTH,expand=True)
all_packages = pip.get_installed_distributions()
for p in all_packages:
    listbox.insert(END,p)
    # p.key 不显示版本号
app.mainloop()