from tkinter import *
from tkinter import ttk             # اختيار متعدد Combobox

hamdy=Tk()
hamdy.geometry('500x500')

############################  button
button_1=Button(hamdy,text='login',font=('courier',15),bg='#B98f10',fg='#17202A',width=11)
button_1.place(x=5,y=200)

button_2=Button(hamdy,text='signin',font=('courier',15),bg='#808FF0',fg='#17202A',width=11)
button_2.place(x=150,y=200)

button_3=Button(hamdy,text='signin', activebackground='black' , activeforeground='white' )
button_3.pack()

button_4=Button(hamdy,
text='signin',
activebackground='red',
activeforeground='white')

button_4.pack()

hamdy.mainloop()