from tkinter import *  #  class & object استدعاء جميع المكتبة

hamdy1=Tk()          #    جاهز داخل المكتبةclass  # لعمل object
hamdy2=Tk()

hamdy1.title('window1')
hamdy2.title('window2')

hamdy1.geometry('300x300+10+10')
hamdy2.geometry('300x300+320+10')

hamdy1.config(background= 'red')
hamdy2.config(background='blue')

hamdy1.mainloop()   # الامر لتنفيذ التشغيل الكود
hamdy2.mainloop()