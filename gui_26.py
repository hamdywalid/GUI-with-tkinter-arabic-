from tkinter import *
import tkinter as tk     ########## خاصية نصوص كبيرة textarea

hamdy=Tk()
hamdy.geometry('500x500')

#t=tk.Text(hamdy,height=7,width=15)   ########## خاصية نصوص كبيرة textarea
t=tk.Text(hamdy) 
t.pack()

learn="""
lets learn html
lets learn css
lets learn php
lets learn sql
python is very easy
"""
t.insert(tk.END,learn)  # gui اضافة الكلام الي 
hamdy.mainloop()