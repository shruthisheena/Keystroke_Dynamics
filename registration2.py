from tkinter import *
from tkinter import messagebox
from login2 import *
from time import time

class regist:
# root = Tk()
 def __init__(self,root):
  self.root= root
  global j
  global totaltime
  global totaltime1
  global totaltime2
  j=0

  root.title("Registration Form")
  root.geometry('500x500')
  #Button(root, text='Reset',width=20,bg='brown',fg='white',command=validation).place(x=180,y=430)
  # Centering Root Window on Screen

  w = 500 # width for the Tk root
  h = 500 # height for the Tk root

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

  self.Uid=StringVar()
  self.Pswd1=StringVar()

  self.label_0 = Label(self.root, text="Registration Form",width=20,font=("Courier New", 20, "bold"),bg='#98fb98',fg='red')

  self.label_0.place(x=90,y=53)
  Button(self.root, text='Submit',width=15,bg='brown',fg='white',command=self.pas).place(x=350,y=180)

 def pas(self):
  global j
  j+=1

  self.label_6 = Label(self.root, text="Password Enter Three Times For Key Strokes",width=50,font=("bold", 10),bg='#98fb98',fg='blue', anchor='w')
  self.label_6.place(x=70,y=380)

  self.label_7 = Label(self.root, text="Confirm Password",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_7.place(x=70,y=430)


  self.entry_6 = Entry(self.root,textvar=self.Pswd1,show='*')
  self.entry_6.place(x=180,y=430)
  exp=''
  self.Pswd1.set(exp)

  def pressed(keyevent):
   global start
   cword = "govind"
   print(cword)
   cwordsize = len(cword)
   cwordlist = tuple(cword)
   cwordfl = str(cwordlist[0])
   cwordll = str(cwordlist[-1])

   tword = self.entry_6.get()
   twordsize = len(tword)
   if twordsize > 0:
    twordlist = tuple(tword)
   twordfl = str(twordlist[0])
   twordll = str(twordlist[-1])
   if cwordsize == 1 and twordsize == 1:
    print("more letters")
   if twordsize == 1 and cwordsize > 1:
    global start
    start = time()
   if twordsize == cwordsize and twordsize != 1:
    if cwordll == twordll:
     stop = time()
     if j==1:
      self.totaltime = stop - start
      print(self.totaltime)
     if j==2:
      self.totaltime1 = stop - start
      print(self.totaltime1)
     if j==3:
      self.totaltime2 = stop - start
      print(self.totaltime2)
  self.entry_6.bind('<KeyRelease>', pressed)
    
  if j<3:
   Button(self.root, text='Confirm',width=15,bg='brown',fg='white',command=self.pas).place(x=350,y=430)
  else:
   Button(self.root, text='End',width=15,bg='brown',fg='white',command=self.cal).place(x=350,y=430)   
 
 def cal(self):
  sum=0
  sum=self.totaltime + self.totaltime1 + self.totaltime2
  #print(sum)
  avg=sum/3
  minavg=avg-0.1
  max_avg=avg+0.1
  print("minavg    " + str(minavg))
  print("maxavg    " + str(max_avg))

  
  



     

if __name__ == '__main__':

 root = Tk()

 application=regist(root)
 #root.geometry('500x500') 
 root.mainloop()





