from tkinter import *

hamdy=Tk()

hamdy.geometry('500x500')
photo = PhotoImage(file="D:\\download_D\\logo.png")
imgl = Label(hamdy,image=photo)
#imgl.place(x=0,y=0)
imgl.pack()

hamdy.mainloop()