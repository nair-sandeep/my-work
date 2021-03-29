from tkinter import *  
from PIL import ImageTk,Image
import random
from tkinter import messagebox 


root = Tk()  
root.configure(bg="#000")
root.geometry('1200x700')
#root.title("Game")  
 


def start():
	uname=name.get()
	if uname!="":
		uname=uname.upper()
		label_user.config(text = uname,bd=10)
		label_sys.place(x=120,y=150)
		sys_score.place(x=275,y=150)
		user_score.place(x=1005,y=150)
		label_user.place(x=850,y=150)
		label_vs.place(x=530,y=100)
		#la.place(x=300,y=300)
		name_entry.place_forget()
		bt_name.place_forget()
		label_name.place_forget()
		

		user()

	else:
		messagebox.showerror("Invalid input", "Please enter a name")



def user():
	var1=StringVar()
	img1 = ImageTk.PhotoImage(Image.open(r'stoneuser.png').resize((120,120)))
	ub1=Button(root,image=img1,activebackground="#000",bg="#000",bd=0,command=stone)
	ub1.image=img1
	ub1.place(x=750,y=250)
	img2 = ImageTk.PhotoImage(Image.open(r'paperuser.png').resize((120,120)))
	ub2=Button(root,image=img2,activebackground="#000",bg="#000",bd=0,command=paper)
	ub2.image=img2
	ub2.place(x=900,y=250)
	img3 = ImageTk.PhotoImage(Image.open(r'sissoruser.png').resize((120,120)))
	ub3=Button(root,image=img3,activebackground="#000",bg="#000",bd=0,command=sissor)
	ub3.image=img3
	ub3.place(x=1050,y=250)

	move= Label(root,text = "Choose Your Move",bg="#000",fg="#6600CC",width=20,height=2,font=('Hardsign',15))
	move.place(x=850,y=400)	

	global l2,win,l1
	l1= Label(root,text = "",bg="#000",fg="#CC0000",width=20,height=2,font=('Brush Pains',22))
	l2= Label(root,text = "",bg="#000",fg="#FFCC00",width=20,height=2,font=('CHrONicLe',20))
	win= Label(root,text = "",bg="#000",fg="#FFCC00",width=20,height=2,font=('Rockidz 3D',35))
	
	global bt
	bt=Button(root,text="RESET",width=15,font=('Brush Pains',20),bg="#000",fg="#00BD17",bd=20,relief="raised",activebackground="#000",activeforeground="red",command=reset)

	
s=0
u=0
def stone():
	global s
	global u
	sys()
	l2.config(text = "STONE")
	if v1=="STONE":
		win.config(text="Draw")
	elif v1=="PAPER":
		win.config(text="You Lose")
		s=s+1
	else:
		win.config(text="You Win")
		u=u+1
	sys_score.config(text=s)
	user_score.config(text=u)
		

def paper():
	global s
	global u
	sys()
	l2.config(text = "PAPER")
	if v1=="STONE":
		win.config(text="You Win")
		u=u+1
	elif v1=="PAPER":
		win.config(text="Draw")
	else:
		win.config(text="You Lose")
		s=s+1
	sys_score.config(text=s)
	user_score.config(text=u)

def sissor():
	global s
	global u
	sys()
	l2.config(text = "SISSOR")
	if v1=="STONE":
		win.config(text="You Lose")
		s=s+1
	elif v1=="PAPER":
		win.config(text="You Win")
		u=u+1
	else:
		win.config(text="Draw")
	sys_score.config(text=s)
	user_score.config(text=u)
	
v1=""
def sys():
	global sys_im
	#global l1
	ch = ['STONE', 'PAPER', 'SISSOR']
	global v1
	v1=random.choice(ch)
	
	#l1= Label(root,text = "",bg="#000",fg="#CC0000",width=20,height=2,font=('Brush Pains',22))
	
	if v1=="STONE":
		#rock()
		img = ImageTk.PhotoImage(Image.open(r'stone.png').resize((150,150))) 
		sys_im = Label(image=img,bd=0)
		sys_im.image = img
		l1.config(text = v1)
	elif v1=="PAPER":
		img = ImageTk.PhotoImage(Image.open(r'paper.png').resize((150,150))) 
		sys_im = Label(image=img,bd=0)
		sys_im.image = img
		l1.config(text = v1)
	else:
		img = ImageTk.PhotoImage(Image.open(r'sissor.png').resize((150,150))) 
		sys_im = Label(image=img,bd=0)
		sys_im.image = img
		l1.config(text = v1)
	sys_im.place(x=150,y=250)
	l1.place(x=100,y=455)
	l2.place(x=820,y=450)
	win.place(x=360,y=400)
	bt.place(x=450,y=600)

#CHrONicLe #Rockidz 3D(BLACK YELLOW) #Rainball #Hardsign #Brush Pains
def reset():

	sys_im.config(image=None,bg='#000')
	sys_im.image = None
	l1.place_forget()
	l2.place_forget()
	sys_score.config(text="0")
	user_score.config(text="0")
	win.place_forget()
	bt.place_forget()
#flat, groove, raised, ridge, solid, or sunken

#TOP
root.title("Game")
label_0=Label(root,text="Welcome to Stone Paper Sissor Game!",width=30,font=('ravie',30),bg="#000",fg="#66fcf1")
label_0.pack(pady=10)#place(x=120,y=0)

#For User name
global name
name=StringVar()
label_name=Label(root,text="ENTER YOUR NAME",width=20,font=('Harligh Brush',20),bg="#000",fg="#CC0000")
label_name.place(x=150,y=160)
name_entry = Entry(bg="#6600CC", fg='#FFCC00',font=('karam',15),bd=10,textvariable=name,relief='groove',width=30)
name_entry.place(x=400, y=150)
bt_name=Button(root,text="Play",width=10,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,relief="raised",activebackground="#000",activeforeground="#FFCC00",command=start)
bt_name.place(x=750,y=130)



#SYS V/S USER 
label_sys=Label(root,text="SYSTEM",width=10,font=('Staincool Base',20),bg="#6600CC",fg="#fff",bd=10,relief="sunken")
label_user=Label(root,text="",width=10,font=('Staincool Base',20),bg="#6600CC",fg="#FFF",bd=0,relief="sunken")
sys_score=Label(root,text="0",width=3,font=('Rockidz 3D',20),bg="#000",fg="#FFCC00",bd=10,relief="sunken")
user_score=Label(root,text="0",width=3,font=('Rockidz 3D',20),bg="#000",fg="#FFCC00",bd=10,relief="sunken")
#label_vs=Label(root,text="V/S",width=10,font=('Lucida Handwriting',30),bg="#000",fg="#6600CC",bd=0,relief="sunken")
imgvs = ImageTk.PhotoImage(Image.open(r'F:\shi\vs.png').resize((100,150))) 
label_vs = Label(image=imgvs,bd=0)
label_vs.image = imgvs


root.mainloop()




