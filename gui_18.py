from tkinter import *
from tkinter import ttk             # اختيار متعدد Combobox

hamdy=Tk()
hamdy.geometry('800x500')

Menubutton_1 = Menubutton(hamdy,text='learn',relief='groove')     # زر متعدد الاختيارات MenuButton
Menubutton_1.pack()                                                #    relief='groove'  شكل الزر

list_of_menu=Menu(Menubutton_1)       # (اسم الزر ) menu = menu اسم 
Menubutton_1['menu']=list_of_menu

list_of_menu.add_checkbutton(label='classic control')  # (label='classic control') سم الزر + add اضافة للقائمة من خلال كتابة الاسم القائمة مع 
list_of_menu.add_checkbutton(label='plc basic')        # (label='plc basic') سم الزر + add اضافة للقائمة من خلال كتابة الاسم القائمة مع 
list_of_menu.add_checkbutton(label='plc advanced')        # (label='plc advanced') سم الزر + add اضافة للقائمة من خلال كتابة الاسم القائمة مع 
list_of_menu.add_checkbutton(label='hmi')        # (label='hmi') سم الزر + add اضافة للقائمة من خلال كتابة الاسم القائمة مع 
list_of_menu.add_checkbutton(label='scada')        # (label='scada') سم الزر + add اضافة للقائمة من خلال كتابة الاسم القائمة مع 

hamdy.mainloop()