from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
#function
def signup_page():
    login_window.destroy()
    import signup
def user_enter(event):
        if UsernameEntry.get() == 'Username':
             UsernameEntry.delete(0,END)
def login_user():
    if UsernameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='muskansql@26')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (UsernameEntry.get(), PasswordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Login successful')

def forget_pass():
    def change_pass():
        if UsernameEntry.get()=='' or PasswordEntry.get()=='' or cnfrmpass_Entry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=window)
        elif newpass_Entry.get() != cnfrmpass_Entry.get():
            messagebox.showerror('Error', 'Password and confirm password are not matching',parent=window)
        else:
                con = pymysql.connect(host='localhost', user='root', password='muskansql@26',database='userdata')
                mycursor = con.cursor()
                query = 'select * from data where username=%s'
                mycursor.execute(query, (UsernameEntry.get()))
                row=mycursor.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Incorrect username ',parent=window)
                else:
                    query='update data set password=%s where username=%s'
                    mycursor.execute(query,(newpass_Entry.get(),UsernameEntry.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success', 'Password is reset,please login with new password')
    window=Toplevel()
    window.title('Change Password')
    bgpic=ImageTk.PhotoImage(file='background.jpg')
    bgLabel=Label(window,image=bgpic)
    bgLabel.grid()
    heading = Label(window, text='RESET PASSWORD', font=('Microsoft Yahel UI Light', 20, 'bold'),
                    bg='white', fg='firebrick')
    heading.place(x=480, y=60)
    heading = Label(window, text='Username', font=('Microsoft Yahel UI Light', 12, 'bold'),
                    bg='white', fg='firebrick')
    heading.place(x=470, y=130)
    UsernameEntry = Entry(window, width=25, font=('Microsoft Yahel UI Light', 11, 'bold'), bd=0, fg='firebrick')
    UsernameEntry.place(x=470, y=160)
    Frame(window, width=250, height=2, bg='firebrick').place(x=470, y=180)

    passwordlabel= Label(window, text='New Password', font=('Microsoft Yahel UI Light', 12, 'bold'),
                    bg='white', fg='firebrick')
    passwordlabel.place(x=470, y=210)
    newpass_Entry = Entry(window, width=25, font=('Microsoft Yahel UI Light', 11, 'bold'), bd=0, fg='firebrick')
    newpass_Entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='firebrick').place(x=470, y=260)

    cnfrmpass_label = Label(window, text='Confirm Password', font=('Microsoft Yahel UI Light', 12, 'bold'),
                          bg='white', fg='firebrick')
    cnfrmpass_label.place(x=470, y=290)
    cnfrmpass_Entry = Entry(window, width=25, font=('Microsoft Yahel UI Light', 11, 'bold'), bd=0, fg='firebrick')
    cnfrmpass_Entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='firebrick').place(x=470, y=340)

    submit = Button(window, text='SUBMIT', font=('open sans', 16, 'bold'), fg='white', bg='firebrick',
                         activeforeground='white'
                         , activebackground='firebrick', cursor='hand2', bd=0, width=19,command=change_pass)
    submit.place(x=470, y=390)

    window.mainloop()
def password_enter(event):
    if PasswordEntry.get() == 'Password':
        PasswordEntry.delete(0, END)

def hide ():
    openeye.config(file='closeye.png')
    PasswordEntry.config(show='*')
    eyeButton.config(command=show)
def show():
    openeye.config(file='openeye.png')
    PasswordEntry.config(show='')
    eyeButton.config(command=hide)
#gui
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable (0,0)
login_window.title('Login Page')
bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(login_window , image=bgImage)
bgLabel.place(x= 0 , y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahel UI Light',25,'bold'),
              bg='white',fg='firebrick')
heading.place(x=600,y=120)
UsernameEntry=Entry(login_window,width=25,font=('Microsoft Yahel UI Light',11,'bold'),bd=0,fg='firebrick')
UsernameEntry.insert(0,'Username')
UsernameEntry.bind('<FocusIn>',user_enter)
UsernameEntry.place(x=605,y=200)
Frame(login_window,width=250,height=2,bg='firebrick').place(x=580,y=222)
PasswordEntry=Entry(login_window,width=25,font=('Microsoft Yahel UI Light',11,'bold'),bd=0,fg='firebrick')
PasswordEntry.insert(0,'Password')
PasswordEntry.bind('<FocusIn>',password_enter)
PasswordEntry.place(x=605,y=260)
Frame(login_window,width=250,height=2,bg='firebrick').place(x=580,y=282)
openeye=PhotoImage(file='openeye.png')
eyeButton =Button (login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)
forgotButton =Button (login_window,text='Forgot Password',bd=0,bg='white',activebackground='white',cursor='hand2'
                      ,font=('Microsoft Yahel UI Light',11,'bold'),fg='firebrick',activeforeground='firebrick',command=forget_pass)
forgotButton.place(x=715,y=295)

loginbutton=Button(login_window,text='LOGIN', font=('open sans',16,'bold'),fg='white',bg='firebrick',activeforeground='white'
                   ,activebackground='firebrick',cursor='hand2',bd=0,width=19,command=login_user)
loginbutton.place(x=578,y=350)

orlabel=Label(login_window,text='---------------------OR---------------------',font=('open sans',12,'bold'),fg='firebrick',bg='white')
orlabel.place(x=583,y=400)
facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

Google_logo=PhotoImage(file='google.png')
GoogleLabel=Label(login_window,image=Google_logo,bg='white')
GoogleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')

twLabel=Label(login_window,image=twitter_logo,bg='white')
twLabel.place(x=740,y=440)

signlabel=Label(login_window,text="Don't have an account",font=('open sans',9,'bold'),fg='firebrick',bg='white')
signlabel.place(x=590,y=500)
newacc_button=Button(login_window,text='Create new account', font=('open sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue'
                   ,activebackground='white',cursor='hand2',bd=0,command=signup_page)
newacc_button.place(x=727,y=500)


login_window.mainloop()
