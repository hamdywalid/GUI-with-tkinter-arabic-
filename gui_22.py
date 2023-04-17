from tkinter import *
from tkinter import ttk
hamdy= Tk()
hamdy.geometry('500x400')

nb= ttk.Notebook(hamdy)         # نوت بوك اقسام البرنامج Notebook
nb.pack()

f1=Frame(nb,width='500',height='50', bg='silver')  #   (العرض و الارتفارع + Notebookالمتغير الخاص ب) الاول ياخذ  frame
nb.add(f1,text='home')                 #         الاول و النص frame عبر المتغير الاول نضيف الي                                             

f2=Frame(nb,width='500',height='50', bg='silver')   #         (العرض و الارتفارع + Notebookالمتغير الخاص ب) الاول ياخذ  frame
nb.add(f2,text='tools')                 #         الاول و النص frame عبر المتغير الاول نضيف الي   

lb1=Label(f1,text='learn python',bg='green')
lb1.pack()
#lb2=Label(f2,text='learn AI',bg='green')
#lb2.pack()

nb.select(f1)            #  يظهر frame اختيار اول   

hamdy.mainloop()