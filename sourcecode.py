#python  clock
from tkinter import *
import time

root = Tk()

root.title("DIGITAL CLOCK")
root.geometry("500x400+0+0")
root.config(bg="grey9")

def clock():
   h = str(time.strftime("%H"))

   m = str(time.strftime("%M"))
   s = str(time.strftime("%S"))
   #print(h,m,s)


   if int(h)>12  and int(m)>0:
       Ilb_NOON.config(text="PM")

   if int(h)>12:
       h = str((int(h)-12))






   Ilb_hr.config(text=h)
   Ilb_min.config(text=m)
   Ilb_sec.config(text=s)

   Ilb_hr.after(200,clock)


Ilb_hr =Label(root,text="12",font = ("Comic Sans MS",45,"bold"),bg="DodgerBLue2",fg="white")
Ilb_hr.place( x=70, y=150, width=100, height=100)

Ilb_hr2 = Label(root,text="HOUR",font=("Comic Sans MS",20,"bold"),bg="steelblue1",fg="white")
Ilb_hr2.place( x=70,y=260,width=100,height=50)

Ilb_min =Label(root,text="00",font = ("Comic Sans MS",45,"bold"),bg="DodgerBLue2",fg="white")
Ilb_min.place( x=200, y=150, width=100, height=100)

Ilb_min2 = Label(root,text="MIN",font=("Comic Sans MS",20,"bold"),bg="steelblue1",fg="white")
Ilb_min2.place( x=200,y=260,width=100,height=50)

Ilb_sec =Label(root,text="00",font = ("Comic Sans MS",45,"bold"),bg="DodgerBLue2",fg="white")
Ilb_sec.place( x=330, y=150, width=100, height=100)

Ilb_sec2 = Label(root,text="SEC",font=("Comic Sans MS",20,"bold"),bg="steelblue1",fg="white")
Ilb_sec2.place( x=330,y=260,width=100,height=50)


Ilb_NOON =Label(root,text="AM",font = ("Comic Sans MS",20,"bold"),bg="VioletRed1",fg="white")
Ilb_NOON.place( x=70, y=320, width=360, height=50)


clock()
root.mainloop()



