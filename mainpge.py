from tkinter import *


from tkinter import messagebox
import tkinter.filedialog
from login2 import *
from registration1 import *

class mainpg:
# root = Tk()
 def __init__(self,root):
  self.root= root
  root.title("WELCOME")
  root.geometry('500x500')
  #Button(root, text='Reset',width=20,bg='brown',fg='white',command=validation).place(x=180,y=430)
  # Centering Root Window on Screen

  w = 600 # width for the Tk root
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

  self.fname=StringVar()
  self.msg=StringVar()
  self.psw =StringVar()
  
  self.label_0 = Label(self.root, text="Key Stroke Based User Authentiction",width=50,font=("Courier New", 15, "bold"),bg='#98fb98',fg='red')

  self.label_0.place(x=30,y=53)


 
  Button(self.root, text='Login',width=15,bg='brown',fg='white',command=self.logform).place(x=230,y=120)
  Button(self.root, text='Signup',width=15,bg='brown',fg='white',command=self.signform).place(x=230,y=180)
 # Button(self.root, text='Analysis',width=15,bg='brown',fg='white',command=self.select_file).place(x=230,y=240)

  
 def logform(self):
  
  #Do the work done by the main of Login2.py
  #Destroy current window
  self.root.destroy()
  #Open new window
  newroot = Tk()
  application = User_Login(newroot)
  newroot.mainloop()

 def signform(self):
  
  #Do the work done by the main of Login2.py
  #Destroy current window
  self.root.destroy()
  #Open new window
  newroot = Tk()
  application = regist(newroot)
  newroot.mainloop()



if __name__ == '__main__':

 root = Tk()

 application=mainpg(root)
 #root.geometry('500x500') 
 root.mainloop()





