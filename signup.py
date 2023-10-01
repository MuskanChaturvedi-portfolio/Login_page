from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import re
def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    cnfrmpassEntry.delete(0,END)
    check.set(0)
def is_valid_email(email):
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern,email):
        return True
    else:
        return  False

def connect_database():
    email = emailEntry.get()
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or cnfrmpassEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif passwordEntry.get() != cnfrmpassEntry.get():
        messagebox.showerror('Error', 'Password Mismatched')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please accept terms & conditions')
    if not is_valid_email(email):
        messagebox.showerror('Error', 'Invalid Email')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='muskansql@26')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue,Please try again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='Use userdata'
            mycursor.execute(query)
            query='create table data (id int auto_increment primary key not null,' \
                  'email varchar(50) ,username varchar(100),password varchar(20))'
            mycursor.execute(query)

        except:
            mycursor.execute('use userdata')

        query = 'select * from data where username=%s'
        mycursor.execute(query, (usernameEntry.get()))
        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username Already exists')
        else:
            query='insert into data(email,username,password) values(%s, %s, %s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signup_window.destroy()
            import signin.py


def login_page():
    signup_window.destroy()
    import signin

signup_window=Tk()
signup_window.title('Sign up page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(signup_window,image=background)
bgLabel.grid()
frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)
heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahel UI Light',18,'bold'),
              bg='white',fg='firebrick')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahel UI Light',10,'bold'),bg='white',fg='firebrick')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry=Entry(frame,width=35,font=('Microsoft Yahel UI Light',10,'bold'),bg='firebrick',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahel UI Light',10,'bold'),bg='white',fg='firebrick')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=35,font=('Microsoft Yahel UI Light',10,'bold'),bg='firebrick',fg='white')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahel UI Light',10,'bold'),bg='white',fg='firebrick')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=35,font=('Microsoft Yahel UI Light',10,'bold'),bg='firebrick',fg='white')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)


cnfrmpassLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahel UI Light',10,'bold'),bg='white',fg='firebrick')
cnfrmpassLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
cnfrmpassEntry=Entry(frame,width=35,font=('Microsoft Yahel UI Light',10,'bold'),bg='firebrick',fg='white')
cnfrmpassEntry.grid(row=8,column=0,sticky='w',padx=25)
check=IntVar()


termsandcondition=Checkbutton(frame,text='I agree to the Terms and Conditions',font=('Microsoft Yahel UI Light',9,'bold'),fg='firebrick',bg='white'
                              ,activebackground='white',activeforeground='firebrick',cursor='hand2' ,variable=check)
termsandcondition.grid(row=9,column=0,padx=15,pady=10)

signupButton=Button(frame,text='SIGNUP',font=('Open sans',16,'bold'),bd=0,fg='white',bg='firebrick'
                    ,activebackground='firebrick',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,padx=25)

alreadyaccLabel=Label(frame,text="Don't have an account",font=('Microsoft Yahel UI Light',9,'bold'),bg='white',fg='firebrick')
alreadyaccLabel.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Log in',font=('Open sans',9,'bold underline'),fg='blue',bg='white'
                    ,activebackground='white',activeforeground='blue',cursor='hand2',bd=0,command=login_page)
loginButton.grid(row=12,column=0,sticky='w',padx=25)
signup_window.mainloop()