from tkinter import *
from tkinter import ttk             # اختيار متعدد Combobox

hamdy=Tk()
hamdy.geometry('500x500')
hamdy.resizable(False,False)
hamdy.title('learn python ')
hamdy.config(background='#34495E')   # color html
hamdy.iconbitmap("D:/download_D/car2.ico")
 ############################ title
title= Label(hamdy,text='login system' , font=('courier',15),bg='#00FFFF',fg='#17202A') 
title.pack(fill=X)
###############################  frame
fr1=Frame(hamdy,width='300',height='350',bg='#808000')
fr1.pack(pady=40)
##############################   image
photo = PhotoImage(file="D:\\download_D\\logo.png")
panel = Label(hamdy,image=photo)
panel.place(x=190,y=40)
############################### label
lb1=Label(fr1,text='username :',font=('courier',15),bg='#808000',fg='#17202A')
lb1.place(x=10,y=100)

lb2=Label(fr1,text='passward :',font=('courier',15),bg='#808000',fg='#17202A')
lb2.place(x=10,y=140)
############################### entry
en1=Entry(fr1)
en1.place(x=130,y=105)
en2=Entry(fr1)
en2.place(x=130,y=145)
############################  button
button_1=Button(fr1,text='login',font=('courier',15),bg='#B98f10',fg='#17202A',width=11)
button_1.place(x=5,y=200)
button_2=Button(fr1,text='signin',font=('courier',15),bg='#808FF0',fg='#17202A',width=11)
button_2.place(x=150,y=200)
############################## check box
c1=Checkbutton(fr1, text='forget passward!',font=('courier',15),bg='#808000')
c1.place(x=40,y=240)

pw=Label(fr1,text='devloped by ROV22' , font=('courier',20),bg='#808000',fg='#17202A') 
pw.place(x=10,y=300)

hamdy.mainloop()