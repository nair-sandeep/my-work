from tkinter import *
import time
import random

root = Tk() 

# set the title 
root.title("COLORGAME") 

# set the size 
root.geometry("700x500")
root.config(bg="salmon")


COLORS = ['black', 'blue', 'gray', 'green', 'purple', 'red', 'white', 'yellow', 'maroon', 'orange', 'pink', 'silver', 'violet']

l0=Label(text="Type the color of the word Not the Word",width=50,font=('ravie',15),bg="#000",fg="#66fcf1")
l0.pack()
Label(root,text="Press Enter to start",font=('Harligh Brush',20),fg="green4").pack()

tim=Label(text="30", font=('Staincool Base', 20), fg='red',bg="cadet blue")
tim.pack(side=RIGHT,anchor=NE)
l11=Label(text="Time : ", font=('Harligh Brush',25),fg="navy",bg="cadet blue")
l11.pack(side=RIGHT,anchor=NE)
sco_l=Label(text="Score : ", font=('Staincool Base', 20), fg='red',bg="cadet blue")
sco_l.pack(side=LEFT,anchor=NW)
sco_n=Label(text="", font=('Harligh Brush',25),fg="navy",bg="cadet blue")
sco_n.pack(side=LEFT,anchor=NW)
Label(text="",bg="salmon").pack()
l2=Label(root,text="",font=('CHrONicLe',35),bg="salmon")
l2.pack()



def color_change():
	global l2,s,sco_n

	if t>0:
		ent.focus_set()
		e=ent.get().upper()
		
		if e==COLORS[1].upper():
			s=s+1
			#print("xxxxxxxxxx")
		
		#print(s)
		#print("ee",e)
		
		random.shuffle(COLORS)
		
		
		l2.config(text=COLORS[0],fg=COLORS[1])
		sco_n.config(text=s)
		ent.delete(0, END)


def start(event):
	if t==30:
		update_clock()

	color_change()



ent=Entry(root)
root.bind('<Return>', start)
ent.pack()


def update_clock():
	global t,tim
	tim.config(text=t)
	#print(t)
	t=t-1
	if t>=0:
		root.after(1000, update_clock)
		#update_clock(now)


s=0
t=30

root.mainloop()