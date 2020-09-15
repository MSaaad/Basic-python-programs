from tkinter import *
import random
import time

root=Tk()
root.geometry('1600x800+0+0')
root.title('management system')
#text_Input= stringVar()

Tops=Frame(root,width=1600,height=50,bg='pink',relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=700,height=700,bg='pink',relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=400,height=700,bg='pink',relief=SUNKEN)
f2.pack(side=RIGHT)
#text_Input= stringVar()
localtime=time.asctime(time.localtime(time.time()))

lblinfo =Label(Tops,font=('arial',50,'bold'),text='restaurant menu',fg='steel blue',bd=10,anchor='w')
lblinfo.grid(row=0,column=0)

lblinfo =Label(Tops,font=('arial',20,'bold'),text=localtime,fg='steel blue',bd=10,anchor='w')
lblinfo.grid(row=1,column=0)

txtdisplay=Entry(f2,font=('arial',20,'bold'), textvariable='stringVar()', bd=30,insertwidth=4,bg='yellow',justify='right')
txtdisplay.grid(columnspan=4)
root.mainloop()
