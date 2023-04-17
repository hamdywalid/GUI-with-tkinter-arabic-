from tkinter import *

hamdy=Tk()
hamdy.geometry('400x400')
  
def pro1():               ### class انشاء    
    pro1= Tk()               ###   متفرع  gui اساسي ثم gui ننشئ 
    botton1=Button(pro1, text='exit',command=pro1.quit)
    botton1.pack() 
   # botton1.mainloop()
    
    
botton1=Button(hamdy,text='my program', command=pro1)   ### function  انشاء نافذة داخل نافذة اخرى بالدوال 
botton1.pack()

hamdy.mainloop()