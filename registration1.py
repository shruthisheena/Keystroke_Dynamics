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

  self.Name=StringVar()
  self.Email=StringVar()
  self.Phno =StringVar()
  self.Uid=StringVar()
  self.Pswd=StringVar()
  self.Pswd1=StringVar()
  
  conn = sqlite3.connect('keystrokedb.db')
  with conn:
   cursor=conn.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS Register(Name TEXT,Email TEXT,Phno TEXT,Username TEXT,Password TEXT,t1 TEXT,t2 TEXT,t3 TEXT,maxt1 TEXT,mint1 TEXT)')


  self.label_0 = Label(self.root, text="Registration Form",width=20,font=("Courier New", 20, "bold"),bg='#98fb98',fg='red')

  self.label_0.place(x=90,y=53)


  self.label_1 = Label(self.root, text="Name",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_1.place(x=70,y=130)

  self.entry_1 = Entry(self.root,textvar=self.Name)
  self.entry_1.place(x=180,y=130)

  self.label_2 = Label(self.root, text="Email",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_2.place(x=70,y=180)

  self.entry_2 = Entry(self.root,textvar=self.Email)
  self.entry_2.place(x=180,y=180)

  self.label_3 = Label(self.root, text="Phone",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_3.place(x=70,y=230)

  c=self.root.register(self.only_numeric_input)
  self.entry_3 = Entry(self.root,textvar=self.Phno,validate="key",validatecommand=(c,'%P'))
  self.entry_3.place(x=180,y=230)


  self.label_4 = Label(self.root, text="User Id",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_4.place(x=70,y=280)

  self.entry_4 = Entry(self.root,textvar=self.Uid)
  self.entry_4.place(x=180,y=280)


  self.label_5 = Label(self.root, text="Password",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_5.place(x=70,y=330)

  self.entry_5 = Entry(self.root,textvar=self.Pswd,show='*')
  self.entry_5.place(x=180,y=330)

  
  Button(self.root, text='Submit',width=15,bg='brown',fg='white',command=self.database).place(x=350,y=180)
  #Button(self.root, text='Reset',width=15,bg='brown',fg='white',command=self.df1).place(x=350,y=230)
  Button(self.root, text='Exit',width=15,bg='brown',fg='white',command=self.logform).place(x=350,y=280)

 def only_numeric_input(self,e):
  #this is allowing all numeric input
  if e.isdigit():
   return True
  #this will allow backspace to work
  elif e=="":
   return True
  else:
   return False

 def logform(self):
  #from login2 import *  
  #Do the work done by the main of Login2.py
  #Destroy current window
  self.root.destroy()
  #Open new window
  newroot = Tk()
  application = User_Login(newroot)
  newroot.mainloop()

 def df1(self):
  exp=''
  self.Name.set(exp)
  self.Email.set(exp)
  self.Phno.set(exp)
  self.Uid.set(exp)
  self.Pswd.set(exp)
   
 def validation(self):
  name1=self.Name.get()
  email=self.Email.get()
  phno1=self.Phno.get()
  uid1=self.Uid.get()
  pswd1=self.Pswd.get()
  valemail=self.checkemail(email)
  ip=len(name1) != 0 and len(email) != 0 and len(phno1) != 0 and len(uid1) != 0 and len(pswd1) != 0 and valemail=="Valid Email"
  return ip

 def checkemail(self,email):  
  regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

  # pass the regualar expression and the string in search() method 
  if(re.search(regex,email)):  
   return "Valid Email"
       
  else:  
   return "Invalid Email"
      

 def checkuser(self,userdet):
  cu=1
  cu1=0
  conn = sqlite3.connect('keystrokedb.db')
  c = conn.cursor()
  # select only the field "username" from the table
  c.execute("SELECT Username FROM Register where Username=?", (userdet,)) 
  #c.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
  # build a set with all names, from the results given as [('name1',), ('name2',), ('name3',)]
  names = {name[0] for name in c.fetchall()}
  #for n in c.fetchall():
  if userdet in names: 
   return cu
  else:
   return cu1

 

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
   cword = self.Pswd.get()
   #print(cword)
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


  name1=self.Name.get()
  email=self.Email.get()
  phno1=self.Phno.get()
  uid1=self.Uid.get()
  pswd2=self.Pswd.get()
  conn = sqlite3.connect('keystrokedb.db')
  with conn:
   cursor=conn.cursor()
  cursor.execute('INSERT INTO Register VALUES(?,?,?,?,?,?,?,?,?,?)',(name1,email,phno1,uid1,pswd2,self.totaltime,self.totaltime1,self.totaltime2,minavg,max_avg))
  conn.commit()
  messagebox.showinfo("Status", "User Details saved success.")
  




     
 def database(self):
  name1=self.Name.get()
  email=self.Email.get()
  phno1=self.Phno.get()
  uid1=self.Uid.get()
  pswd2=self.Pswd.get()
##  conn = sqlite3.connect('keystrokedb.db')
##  with conn:
##   cursor=conn.cursor()
##  cursor.execute('CREATE TABLE IF NOT EXISTS Register(Name TEXT,Email TEXT,Phno TEXT,Username TEXT,Password TEXT,t1 TEXT,t2 TEXT,t3 TEXT,maxt1 TEXT,mint1 TEXT)')

  ip1=self.validation()   
  if self.checkuser(uid1) == 1:
   messagebox.showinfo("Status", "User Exists")            
  else:
   if ip1==1:
##    cursor.execute('INSERT INTO Register(Name,Email,Phno,Username,Password)VALUES(?,?,?,?,?)',(name1,email,phno1,uid1,pswd2))
##    conn.commit()
    messagebox.showinfo("Status", "User Details ok .keystroke checks....")
    self.pas() 
   else:
    messagebox.showinfo("Status", "All fields are mandatory and Give Correct Values.")

if __name__ == '__main__':

 root = Tk()

 application=regist(root)
 #root.geometry('500x500') 
 root.mainloop()





