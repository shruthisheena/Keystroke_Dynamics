from tkinter import *
import sys, string, os

import sqlite3
from tkinter import messagebox
##from mainpg import *
from time import time


class User_Login:
# root = Tk()
 def __init__(self,root):
  self.root= root
  global j
  global totaltime
  j=0

  root.title("Login Form")
  root.geometry('250x250') 
  #Button(root, text='Reset',width=20,bg='brown',fg='white',command=validation).place(x=180,y=430)
  # Centering Root Window on Screen

  w = 350 # width for the Tk root
  h = 300 # height for the Tk root

  # get screen width and height
  ws = root.winfo_screenwidth() # width of the screen
  hs = root.winfo_screenheight() # height of the screen

  # calculate x and y coordinates for the Tk root window
  x = (ws/2) - (w/2)
  y = (hs/2) - (h/2)


  root["bg"] = '#98fb98'
  # set the dimensions of the screen 
  # and where it is placed
  root.geometry('%dx%d+%d+%d' % (w, h, x, y))

  conn = sqlite3.connect('keystrokedb.db')
  with conn:
   cursor=conn.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS Register(Name TEXT,Email TEXT,Phno TEXT,Username TEXT,Password TEXT,t1 TEXT,t2 TEXT,t3 TEXT,maxt1 TEXT,mint1 TEXT)')

  self.Uid=StringVar()
  self.Pswd=StringVar()
  
  self.label_0 = Label(self.root, text="Login Form",width=20,font=("Courier New", 20, "bold"),bg='#98fb98',fg='red')
  self.label_0.place(x=30,y=13)
  self.label_4 = Label(self.root, text="User Id",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_4.place(x=35,y=50)
  self.entry_4 = Entry(self.root,textvar=self.Uid)
  self.entry_4.place(x=115,y=50)
  Button(self.root, text='CheckUser',width=10,bg='brown',fg='white',command=self.leavedf1).place(x=250,y=50)
 

  
  self.label_5 = Label(self.root, text="Password",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_5.place(x=35,y=100)
  

  self.entry_5 = Entry(self.root,textvar=self.Pswd,show='*',state='disabled')
  self.entry_5.place(x=115,y=100)
 

  def pressed(keyevent):
   global start
   
   cword = self.pwdd
  # print(cword)
   cwordsize = len(cword)
   cwordlist = tuple(cword)
   cwordfl = str(cwordlist[0])
   cwordll = str(cwordlist[-1])
   #print(cwordll)

   tword = self.entry_5.get()
   twordsize = len(tword)
   if twordsize > 0:
    twordlist = tuple(tword)
   twordfl = str(twordlist[0])
   twordll = str(twordlist[-1])

   if twordsize == 1 and cwordsize > 1:
    global start
    start = time()
   if twordsize == cwordsize and twordsize != 1:
    if cwordll == twordll:
     stop = time()
     self.totaltime = stop - start
     print(self.totaltime)
   if twordsize > cwordsize :
    messagebox.showinfo("Status","Password incorrect.")
    self.root.destroy()
    
  self.entry_5.bind('<KeyRelease>', pressed)
    

  Button(self.root, text='Login',width=10,bg='brown',fg='white',command=self.database).place(x=30,y=150)
  Button(self.root, text='Cancel',width=10,bg='brown',fg='white',command=self.close_window).place(x=135,y=150)
##  Button(self.root, text='RecoverPSW',width=10,bg='brown',fg='white',command=self.sendmail1).place(x=210,y=150)

 
 
 def close_window (self): 
    self.root.destroy()

   

 def leavedf1(self):
  self.uid1=self.Uid.get()
  ip=len(self.uid1) != 0
  if ip == 1:
   conn = sqlite3.connect('keystrokedb.db')
   c = conn.cursor()
   c.execute("SELECT Username,Password FROM Register where Username=?", (self.uid1,)) 
   vall=c.fetchall();
   vall = dict(vall)
   #print(vall)
   if self.uid1 in vall: 
    self.pwdd=vall[self.uid1]
    self.entry_5.configure(state='normal')
    self.entry_4.configure(state='disabled')
   else:
    messagebox.showinfo("Status","User id does not exist")
    


 def database(self):
  uid1=self.Uid.get()
  pswd1=self.Pswd.get()
  t1=0.0
  t2=0.0
  conn = sqlite3.connect('keystrokedb.db')
  c = conn.cursor()
  c.execute("SELECT maxt1,mint1 FROM Register where Username=?", (self.uid1,)) 
  rows=c.fetchall();
  for row in rows:
   t1=float(row[0])
   t2=float(row[1])
   print(str(t1))
   print(str(t2))
  ip1=len(pswd1) != 0
  
  
  if ip1 ==1:
   if self.pwdd ==pswd1:
    if t1<=self.totaltime and self.totaltime<=t2:
     messagebox.showinfo("Status", "Login Sucessful")
    else:
     messagebox.showinfo("Status", "Key Stroke Not Matched.Login UnSucessful")
   else:
    messagebox.showinfo("Status", "Invalid PSW")
    
  else:
   messagebox.showinfo("Status", "All fields are mandatory")

if __name__ == '__main__':

 root = Tk()
 #root = Tk()
 application=User_Login(root)
 
 root.mainloop()





