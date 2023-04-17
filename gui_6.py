from tkinter import *  #  class & object استدعاء جميع المكتبة

hamdy=Tk()          #    جاهز داخل المكتبةclass  # لعمل object

hamdy.geometry('400x500+500+200')    # (width x height + left + top)لتحكم في العرض و الارتفاع

hamdy.resizable(False ,True)          #  F&T منع المستخدم من التحكم في العرض و الارتفاع حسب الحالة 

hamdy.title('learn python tkinter')    #   تغيير العنوان 

hamdy.config(background='yellow')        # التحكم في خاصية الالوان خلفية _ الشاشة

hamdy.iconbitmap("D:/download_D/car2.ico")                       # لتحكم في ايقونة البرنامج مع المسار ؤ     

hamdy.mainloop()   # الامر لتنفيذ التشغيل الكود  


             # command line علي  run لعمل 
             # cd DESKTOP
             # dir
             # cd Jeston
             # dir
             # cd GUI with tkinter (arabic)
             #dir
             #python3 gui_6.py    # C:\Users\DELL\Desktop\Jeston\GUI with tkinter (arabic) المسار في النهاية
            