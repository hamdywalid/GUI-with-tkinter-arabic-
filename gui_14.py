from tkinter import *
from tkinter import ttk             # اختيار متعدد Combobox

hamdy=Tk()
hamdy.geometry('800x500')

cmbol =ttk.Combobox(hamdy,                # اختيار متعدد Combobox
value=('male','female','1','2')            # العناصر
)

cmbol.place(x=1,y=1)                        #  place

cmbo2 =ttk.Combobox(hamdy,value=('claasic control','plc1','plc2','hmi','scada'),state='readonly')                # اختيار متعدد Combobox
         
cmbo2.place(x=120,y=30)


hamdy.mainloop()