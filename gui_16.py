from tkinter import *
from tkinter import ttk             # اختيار متعدد Combobox

hamdy=Tk()
hamdy.geometry('800x500')

r1= ttk.Radiobutton(hamdy,text='on1',value=1)   ### زر الاختيار راديو Radiobutton
r1.pack()          # للعرض

r2= ttk.Radiobutton(hamdy,text='off1',value=2)   ### زر الاختيار راديو Radiobutton
r2.pack()         # للعرض

r3= ttk.Radiobutton(hamdy,text='stop',value=3)   ### زر الاختيار راديو Radiobutton
r3.pack()        # للعرض

hamdy.mainloop()