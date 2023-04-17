from tkinter import *
from tkinter import ttk             # اختيار متعدد Combobox

hamdy=Tk()
hamdy.geometry('800x500')

r1= ttk.Radiobutton(hamdy,text='Start_F',value=1)   ### زر الاختيار راديو Radiobutton
r1.pack()          # للعرض

r2= ttk.Radiobutton(hamdy,text='Start_R',value=2)   ### زر الاختيار راديو Radiobutton
r2.pack()         # للعرض

r3= ttk.Radiobutton(hamdy,text='_STOP_',value=3)   ### زر الاختيار راديو Radiobutton
r3.pack()        # للعرض

c1= Checkbutton(hamdy,text='OL_1')   ## تحديد متعدد الاختيار checkbutton
c1.pack()
c2= Checkbutton(hamdy,text='OL_2')   ## تحديد متعدد الاختيار checkbutton
c2.pack()
c3= Checkbutton(hamdy,text='OL_3')   ## تحديد متعدد الاختيار checkbutton
c3.pack()
c4= Checkbutton(hamdy,text='OL_4')   ## تحديد متعدد الاختيار checkbutton
c4.pack()


hamdy.mainloop()