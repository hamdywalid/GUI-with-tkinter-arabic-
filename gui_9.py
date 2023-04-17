from tkinter import *  #  class & object استدعاء جميع المكتبة

hamdy1=Tk()          #    جاهز داخل المكتبةclass  # لعمل object
hamdy2=Tk()

hamdy1.lift()            #  لجعلها النافذة الاساسية
hamdy1.state('normal')   #        حالة النافذة عادية

#hamdy2.iconify()        #  جعل النافذة مصغرة
#hamdy2.lower()            #  النافذة مخفية
hamdy2.state('iconic')  # iconify()  تساوي 

hamdy2.state('withdrawn')   # لا تظهر ابدا

hamdy1.title('window1')
hamdy2.title('window2')

hamdy1.geometry('300x300+10+10')
hamdy2.geometry('300x300+320+10')

hamdy1.config(background= 'red')
hamdy2.config(background='blue')

hamdy1.mainloop()   # الامر لتنفيذ التشغيل الكود
hamdy2.mainloop()