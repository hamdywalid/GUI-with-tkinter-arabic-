from tkinter import *
from tkinter import messagebox  ##  استدعاء  لعمل رسالة
hamdy=Tk()
hamdy.geometry('500x500')

def info():        ##     عمل دالة لتكوين الرسالة معلومات
    messagebox.showinfo('info', 'learn pyhton tkinter')

#def info():        ##  عمل دالة لتكوين الرسالة معلومات وسؤال موافق او لا
    messagebox.askokcancel('info', 'learn pyhton tkinter')

#def info():        ##  عمل دالة لتكوين الرسالة معلومات وسؤال موافق او لا
    messagebox.askquestion('info', 'learn pyhton tkinter')

#def info():        ## عمل دالة لتكوين الرسالة 
    messagebox.showwarning('info', 'learn pyhton tkinter')

#def info():        ## عمل دالة لتكوين الرسالة 
    messagebox.askyesno('info', 'learn pyhton tkinter')

#def info():        ## عمل دالة لتكوين الرسالة 
    messagebox.askretrycancel('info', 'learn pyhton tkinter')

button1=Button(hamdy,text='information', command=info)  ### command=info
button1.pack()
hamdy.mainloop()