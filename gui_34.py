from tkinter import *
hamdy=Tk()
hamdy.geometry('500x500')

label1=Label(hamdy,text='class' ,font=('Times New Roman',12,'underline'))  ## جمالية الخطوط fonts
label1.pack()

label2=Label(hamdy,text='plc' ,font=('Helvatica',12,'bold'))  ## جمالية الخطوط fonts
label2.pack()

label3=Label(hamdy,text='plc' ,font=('Impact',12,'italic'))  ## جمالية الخطوط fonts
label3.pack()

hamdy.mainloop()