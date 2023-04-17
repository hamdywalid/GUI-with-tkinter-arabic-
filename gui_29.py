from tkinter import *

class TK:            ### class انشاء  
    def __init__(self, hamdy):   ###  يعني اسم محجوز init ==constractor  انشاء دالة و
       self.hamdy=hamdy          ###   l gui اساسي ثم gui ننشئ  
       self.hamdy.geometry('400x400')
       self.hamdy.title('my program')
       
         
hamdy=Tk()

ob=TK(hamdy)

hamdy.mainloop()