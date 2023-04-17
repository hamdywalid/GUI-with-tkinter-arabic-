from tkinter import *
#from tkinter import ttk             # اختيار متعدد Combobox

hamdy=Tk()
hamdy.geometry('500x500')

photo =PhotoImage(file= r"c:\\users\\dell\\desktop\\calc.png") #  انشاء زر بخلفية صورة button image

res=photo.subsample(10,8) #   تغيير حجم الصورة و كل ما ازيد في الارقام تصغر الصورة

button_1=Button(hamdy,text='learn python',image=res, compound=TOP,width=150,height=150)   
button_1.pack()      #  LIFT او TOP  و مكان ظهور النص في او تمركز النص res الصورة من متغير   


hamdy.mainloop()