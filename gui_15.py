from tkinter import *
from tkinter import ttk             # اختيار متعدد Combobox

hamdy=Tk()
hamdy.geometry('800x500')

lis1 =Listbox(hamdy,width=20,height=20)                # ليستة بيانات Listbox
lis1.insert(0,'one','two','three','four','five','six','seven')    #   ترتيب الفهرس يبدا من الصفر
lis1.insert(8,'plc')
lis1.insert(9,'plc2')

lis1.pack()

hamdy.mainloop()