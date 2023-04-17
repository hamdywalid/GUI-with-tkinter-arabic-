from tkinter import *
from tkinter import ttk             # اختيار متعدد Combobox

hamdy=Tk()
hamdy.geometry('800x500')

Menubar= Menu(hamdy)     #  انشاء قوائم للبرنامج Menu           # file انشاء قائمة 
                                               
list_of_menu=Menu(Menubar, tearoff=0)       # (اسم الزر ) menu = menu اسم 

Menubar.add_cascade(label='file',menu=list_of_menu)    #   للقائمة (label) اضافة عنوان  

list_of_menu.add_command(label='classic control')  # (label='classic control') سم الزر + add اضافة للقائمة من خلال كتابة الاسم القائمة مع 
list_of_menu.add_command(label='plc basic')        # (label='plc basic') سم الزر + add اضافة للقائمة من خلال كتابة الاسم القائمة مع 
list_of_menu.add_command(label='plc advanced')        # (label='plc advanced') سم الزر + add اضافة للقائمة من خلال كتابة الاسم القائمة مع 
list_of_menu.add_command(label='hmi')        # (label='hmi') سم الزر + add اضافة للقائمة من خلال كتابة الاسم القائمة مع 
list_of_menu.add_command(label='scada')        # (label='scada') سم الزر + add اضافة للقائمة من خلال كتابة الاسم القائمة مع 

list_of_menu.add_separator()          # لعمل خط عند الوقوف علي اي من العتاصر

list_of_menu.add_command(label='Exit',command=hamdy.quit)  # command=hamdy.quit اضافة الي القائمة Exit و اعطاء امر الغلق

hamdy.config(menu=Menubar)            # ( اسم المتغير =menu)config لعرض القامة من خلال 

hamdy.mainloop()