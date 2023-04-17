from tkinter import *

hamdy=Tk()
hamdy.geometry('800x500')

fr1 = Frame(width='390',height=499,bg='red')  # لتقسيم الشاشة 
fr1.place(x=1,y=1)                     #  مكان الاطار من خلال ابعاد الشاشة
#fr1.place(x=210,y=100)                  # استدعاء المتغير

fr2 = Frame(width='390',height=499,bg='blue')  # لتقسيم الشاشة 
fr2.place(x=400,y=1)                          #       يظهر من الاحادثياتplace( , )

###variable = tool(master,option)
button1=Button(fr1,text='button1',width='40',height='1',fg='black',bg='yellow')  
button1.place(x=10,y=10)             #  frame  المسافة حسب 

button2=Button(fr2,text='button2',width='30',height='1',fg='black',bg='pink' , cursor='heart')   #  عند الضغط علي الزر mouse شكل   =cursor
button2.place(x=10,y=10) 

label1=Label(fr1,text='hello1',fg='black',bg='green',font=20) 
label1.place(x=10,y=40)

label2=Label(fr2,text='hello2',fg='black',bg='green',font=20)
label2.place(x=10,y=40)

en1 = Entry(fr1)                  #  fr1    للكتابة داخلة  Entry
en1.place(x=80,y=45)              #     الابعاد  Entry 

en2 = Entry(fr1,fg='white',bg='black')                  #  fr1    للكتابة داخلة  Entry
en2.place(x=10,y=100)


en3 = Entry(fr2,justify='center',font=20)         #  fr2   للكتابة داخلة  Entry    
en3.place(x=80,y=45)                       #  الكتابة من المنتصف =  justify 


hamdy.mainloop()