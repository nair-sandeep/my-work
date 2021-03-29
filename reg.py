from tkinter import *
import os
from tkinter import messagebox


main_screen=Tk()
main_screen.title("Select your Choice")
main_screen.geometry("300x250")


def register():
	global register_screen
	register_screen=Toplevel(main_screen)
	register_screen.title("Register")
	register_screen.geometry("300x250")

	global username
	global password	
	global username_entry
	global password_entry
	
	username=StringVar()
	password=StringVar()
	Label(register_screen,text='Enter Your Details Below',bg='blue').pack()
	Label(register_screen,text="").pack()
	username_label=Label(register_screen,text="Username *")
	username_label.pack()
	username_entry=Entry(register_screen,textvariable=username)
	username_entry.pack()
	password_label=Label(register_screen,text="Password *")
	password_label.pack()
	password_entry=Entry(register_screen,textvariable=password,show='*')
	password_entry.pack()
	Label(register_screen,text="").pack()
	Button(register_screen,text="REGISTER",width=18,height=1,bg='blue',command=register_user).pack()


def login():
	global login_screen
	login_screen=Toplevel(main_screen)
	login_screen.geometry('300x250')
	login_screen.title("LOGIN")
	
	global username_verify
	global password_verify
	global username_login_entry
	global password_login_entry
	
	username_verify=StringVar()
	password_verify=StringVar()
	Label(login_screen,text="Enter Login Details").pack()
	Label(login_screen,text="").pack()
	Label(login_screen,text="username *").pack()
	username_login_entry=Entry(login_screen,textvariable=username_verify)
	username_login_entry.pack()
	Label(login_screen,text="").pack()
	Label(login_screen,text="Password *").pack()
	password_login_entry=Entry(login_screen,textvariable=password_verify,show='*')
	password_login_entry.pack()
	Label(login_screen,text="").pack()
	Button(login_screen,text='Login',width=10,height=1,command=login_verify).pack()


def register_user():
	username_info=username.get()
	password_info=password.get()
	if username_info != "" and password_info != "":
		print(username_info,password_info)
		f1=open("username_info","w+")
		f1.write(username_info+"/n")
		f1.write(password_info)
		f1.close()
		Label(register_screen,text="Registration Sucess",fg="red",font=("calibri",11)).pack()
		messagebox.showinfo("Success", "Login_Sucessful")
	else:
		Label(register_screen,text="Registration Failed",fg="red",font=("calibri",11)).pack()
		messagebox.showwarning("Blank", "All the fields are mandatory")
	username_entry.delete(0,END)
	password_entry.delete(0,END)


def login_verify():

	#Label(register_screen,text="For Login",fg="red",font=("calibri",11)).pack()
    username_info = username_verify.get()
    password_info = password_verify.get()
    print(username_info, password_info)
    print(type(username_info),"/n")
    f2 = open("username_info", "r+")
    sr = f2.read()
    s = sr
    print("Read String is : ", sr)
    f2.close()
    print("Closed or not : ", f2.closed)
    print(type(s))
    c=s.split("/n")
    print(c)

    if username_info != "" and password_info != "":
        if c[0] == username_info and c[1] == password_info:
            Label(login_screen, text="Login Success", fg="red", font=("calibri", 11)).pack()
            messagebox.showinfo("Success", "Login_Sucessful")
        else:
            Label(login_screen, text="Invalid Details", fg="red", font=("calibri", 11)).pack()
            messagebox.showerror("Failed", "Invalid Details")
    else:
        messagebox.showwarning("Blank", "All the fields are mandatory")

Button(main_screen,text="register",width=18,height=1,bg='blue',command=register).pack()
Button(main_screen,text="Login",width=18,height=1,bg='blue',command=login).pack()

main_screen.mainloop()
