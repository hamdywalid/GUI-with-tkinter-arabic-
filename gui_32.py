from tkinter import *
hamdy=Tk()
hamdy.geometry('500x500')

botton1=Button(hamdy,text='error', bitmap='error')   ####  ايقونات الازرار التوضيحية Bitmap
botton1.pack()
botton2=Button(hamdy,text='hourglass', bitmap='hourglass')  
botton2.pack()
botton3=Button(hamdy,text='info', bitmap='info')  
botton3.pack()
botton4=Button(hamdy,text='warning', bitmap='warning')  
botton4.pack()
botton5=Button(hamdy,text='question', bitmap='question')  
botton5.pack()
botton6=Button(hamdy,text='gray12', bitmap='gray12')  
botton6.pack()
botton7=Button(hamdy,text='gray25', bitmap='gray25')  
botton7.pack()
#botton8=Button(hamdy,text='gray50', cursor='gray50')  
#botton8.pack()


hamdy.mainloop()



