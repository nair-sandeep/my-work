from tkinter import *  


root = Tk()  
root.configure(bg="#000")
root.title("Calculator")
#root.iconbitmap(calculator.ico)
root.geometry('560x620')
root.resizable(0, 0)



def keyy(item): 
    global expression
    expression = expression + str(item)
    eq.set(expression)


def total():
	global expression
	if expression!="":
		try:
			result = str(eval(expression)) 
			eq.set(result)
			expression = ""
		except:
			eq.set('error')
			expression = " "


def clr(): 
    global expression 
    expression = "" 
    eq.set("")


expression = ""
eq=StringVar()
val = Entry(root,bg="#000", fg='#fff',font=('19th Century Renegade',22),bd=10,textvariable=eq,relief='groove',width=30,justify=RIGHT)

val.grid(row=0,columnspan=4,ipady=5)




Button(root,text="7",width=6,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy(7)).grid(row=1,column=0)
Button(root,text="8",width=6,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy(8)).grid(row=1,column=1)
Button(root,text="9",width=6,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy(9)).grid(row=1,column=2)
Button(root,text="+",width=7,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy('+')).grid(row=1,column=3)

Button(root,text="4",width=6,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy(4)).grid(row=2,column=0)
Button(root,text="5",width=6,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy(5)).grid(row=2,column=1)
Button(root,text="6",width=6,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy(6)).grid(row=2,column=2)
Button(root,text="-",width=7,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy('-')).grid(row=2,column=3)

Button(root,text="1",width=6,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy(1)).grid(row=3,column=0)
Button(root,text="2",width=6,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy(2)).grid(row=3,column=1)
Button(root,text="3",width=6,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy(3)).grid(row=3,column=2)
Button(root,text="*",width=7,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy('*')).grid(row=3,column=3)

Button(root,text="0",width=14,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy(0)).grid(row=4,column=0,columnspan=2)
Button(root,text=".",width=6,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy('.')).grid(row=4,column=2)
Button(root,text="/",width=7,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: keyy('/')).grid(row=4,column=3)

Button(root,text="clear",width=14,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: clr()).grid(row=5,column=0,columnspan=2)
Button(root,text="=",width=14,height=2,font=('Panton Rust Heavy Gr Sh',20),bg="#FFCC00",fg="#000",bd=10,cursor = "hand2",relief="raised",activebackground="#000",activeforeground="#FFCC00",command = lambda: total()).grid(row=5,column=2,columnspan=2)
	




root.mainloop()