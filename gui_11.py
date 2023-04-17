from tkinter import *

hamdy=Tk()
hamdy.geometry('800x500')

fr1 = Frame(width='390',height=499,bg='red')  # لتقسيم الشاشة 
fr1.place(x=1,y=1)                     #  مكان الاطار من خلال ابعاد الشاشة
#fr1.place(x=210,y=100)                  # استدعاء المتغير

fr2 = Frame(width='390',height=499,bg='blue')  # لتقسيم الشاشة 
fr2.place(x=400,y=1)                          #       يظهر من الاحادثياتplace( , )

###variable = tool(master,option)
button1=Button(fr1,text='button1',fg='black',bg='white')  
button1.place(x=1,y=1)             #  frame  المسافة حسب 

button2=Button(fr2,text='button2',fg='black',bg='white' , cursor='heart')   #  عند الضغط علي الزر mouse شكل   =cursor
button2.place(x=1,y=1) 

hamdy.mainloop()

