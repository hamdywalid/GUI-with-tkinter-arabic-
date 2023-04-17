from tkinter import *
from tkinter import ttk             # اختيار متعدد Combobox

hamdy=Tk()
hamdy.geometry('500x400')

sp1=Spinbox(hamdy, from_=0, to =100) ##  عداد الارقام Spinbox
sp1.pack()

sp2=Spinbox(hamdy, from_=20, to =40) ##  عداد الارقام Spinbox
sp2.pack()

enr =Entry(hamdy)
enr.pack()

hamdy.mainloop()