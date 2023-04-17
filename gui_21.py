from tkinter import *

hamdy= Tk()
hamdy.geometry('500x400')

sc1 = Scrollbar(hamdy, orient=VERTICAL)   #انشاء سكرول بار Scrollbar
sc1.pack(side=RIGHT , fill=Y)             # fill=Y نضع VERTICAL # side=RIGHT مكان الظهوريسار ولا يمين

sc2 = Scrollbar(hamdy, orient=HORIZONTAL)   #انشاء سكرول بار Scrollbar
sc2.pack(side=BOTTOM , fill=X)           # fill=X نضع HORIZONTAL # side=BOTTOM   مكان الظهورن الاسفل

hamdy.mainloop()