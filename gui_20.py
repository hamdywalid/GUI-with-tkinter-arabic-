from tkinter import *  #  class & object استدعاء جميع المكتبة

hamdy=Tk()          #    جاهز داخل المكتبةclass  # لعمل object
hamdy.geometry('500x400')    # (width x height + left + top)لتحكم في العرض و الارتفاع
                                         
                                         
  #تستخدم في حالة عمل عداد لتجكم في الصوت او مستوي الاضائة
  
  
sc1 = Scale(hamdy, from_=1, to=100 , orient=VERTICAL  )  # العداد حاصية Scale التعامل مع الارقام
sc1.place(x=10,y=10)                                   #    orient=HORIZONTAL  من 1 حتي 100 و نظام العدد  

sc2 = Scale(hamdy, from_=1, to=100 , orient=VERTICAL  )  # العداد حاصية Scale التعامل مع الارقام
sc2.place(x=100,y=10)                                   #    orient=HORIZONTAL  من 1 حتي 100 و نظام العدد 

sc3 = Scale(hamdy, from_=1, to=100 , orient=VERTICAL  )  # العداد حاصية Scale التعامل مع الارقام
sc3.place(x=190,y=10)                                   #    orient=HORIZONTAL  من 1 حتي 100 و نظام العدد 


hamdy.mainloop()   # الامر لتنفيذ التشغيل الكود