from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        self.root=root
        self.pack(fill=BOTH, expand=1)
        self.root.wm_title("Login")
        self.root.geometry("1202x632")
        self.root.resizable(False,False)

        global username_verify
        global passcode_verify
        global level_verify
 
        username_verify=StringVar()
        passcode_verify=StringVar()
        level_verify=StringVar()
 
        global username_entry
        global passcode_entry
        global level_entry
        
        #load=Image.open("books.png")
        render=ImageTk.PhotoImage(load)
        img=Label(self, image=render)
        img.image=render
        img.place(x=0, y=0)

        Frame_login=Frame(self.root,bg="white",highlightbackground="#c4652b",highlightthickness=5)
        Frame_login.place(x=150,y=150,height=340,width=500)
        
        title=Label(Frame_login,text="Login Here", font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=72,y=20)
        desc=Label(Frame_login,text="Staff Login Gate", font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=72,y=80)

        lbl_user=Label(Frame_login,text="Username", font=("goudy old style",15,"bold"),fg="gray",bg="white").place(x=72,y=110)
        self.txt_user=Entry(Frame_login,textvariable=username_verify,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=72,y=140,width=350,height=35)

        lbl_passcode=Label(Frame_login,text="Passcode", font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=72,y=180)
        self.txt_passcode=Entry(Frame_login,textvariable=passcode_verify,show='*',font=("times new roman",15),bg="lightgray")
        self.txt_passcode.place(x=72,y=208,width=350,height=35)
        
        def login_success():
            global login_success_screen
            login_success_screen=Toplevel(Frame_login)
            login_success_screen.title("User Action Gate")
            login_success_screen.geometry("500x340")
            login_success_screen.resizable(False,False)
            login_success_screen.configure(bg="white")
            login_success_screen.configure(highlightbackground="#c4652b")
            login_success_screen.configure(highlightthickness=5)
            result.config(text="")

            title=Label(login_success_screen,text="Login Successful", font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=72,y=20)
            desc=Label(login_success_screen,text="User Action Gate", font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=72,y=80)

            def sales_request():
                login_success_screen.destroy()
                login_success_screen.update()

            def database_request():
                if self.user_level >= "2":
                    login_success_screen.destroy()
                    login_success_screen.update()
                else:
                  access.config(text="Access Denied")
                        
            Sales_button=Button(login_success_screen,command=sales_request,text="Request Sales (1)",fg="white",bg="#d77337",bd=0,font=("times new roman",20,"bold")).place(x=72,y=120,width=345)

            Database_button=Button(login_success_screen,command=database_request,text="Request Database (2)",fg="white",bg="#d77337",bd=0,font=("times new roman",20,"bold")).place(x=72,y=185,width=345)

            Staff_button=Button(login_success_screen,text="Request Staff (3)",fg="white",bg="#d77337",bd=0,font=("times new roman",20,"bold")).place(x=72,y=250,width=345)
 
        def passcode_not_recognised():
            result.config(text="Login Unsuccessful: Passcode Not Recognised", fg="red")
   
        def user_not_found():
            result.config(text="Login Unsuccessful: User Not Found", fg="red")

        result = Label(Frame_login, bg="white", font=("times new roman", 12))
        result.pack()
 
        def delete_login_success():
            login_success_screen.destroy()
 
        def delete_passcode_not_recognised():
            passcode_not_recog_screen.destroy()
 
        def delete_user_not_found_screen():
            user_not_found_screen.destroy()
                
        def login_verify():
            username1 = username_verify.get()
            passcode1 = passcode_verify.get()
            if os.path.exists(username1):
                with open(username1) as file1:
                    credentials = file1.read().splitlines()
                if passcode1 in credentials:
                    self.user_level = credentials[-1] # save user level
                    login_success()
                else:
                    passcode_not_recognised()
            else:
                user_not_found()

        
        def create_registration():
            top = tk.Toplevel(root)
            top.title("Registration")
            top.geometry("500x450")
            top.resizable(False,False)
            top.configure(bg="white")
            top.configure(highlightbackground="#c4652b")
            top.configure(highlightthickness=5)

            global username
            global passcode
            global level
            global username_entry
            global passcode_entry
            global level_entry
            username=StringVar()
            passcode=StringVar()
    
            title=Label(top,text="Register Here", font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=72,y=20)
            desc=Label(top,text="User Registration Area", font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=72,y=80)

            lbl_user=Label(top,text="Username", font=("goudy old style",15,"bold"),fg="gray",bg="white").place(x=72,y=110)
            self.txt_user=Entry(top,textvariable=username,font=("times new roman",15),bg="lightgray")
            self.txt_user.place(x=72,y=140,width=350,height=35)
    
            lbl_passcode=Label(top,text="Passcode", font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=72,y=180)
            self.txt_passcode=Entry(top,textvariable=passcode,show='*',font=("times new roman",15),bg="lightgray")
            self.txt_passcode.place(x=72,y=208,width=350,height=35)
    
            lbl_level=Label(top,text="Level", font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=72,y=250)
            level = StringVar(top)
            level.set("")

            w = OptionMenu(top, level, "1", "2", "3")
            w.pack()
            w.place(x=72,y=280)
            w.configure(bd=0)

            def register_user():
 
                username_info = username.get()
                passcode_info = passcode.get()
                level_info = level.get()

                if level_info and username_info and passcode_info:
                    if os.path.exists(username_info):
                        result.config(text="Registration Unsuccessful: User Already Exists", fg="red")
                    else:
                        with open(username_info, "w") as f:
                            f.write("\n".join([username_info, passcode_info, level_info]))
                        result.config(text="Registration Successful", fg="green")
                else:
                    result.config(text="Registration Unsuccessful: Please Input All Information", fg="red")
    

            result = Label(top, bg="white", font=("times new roman", 12))
            result.pack()
                    
            Submit_button=Button(top,command=register_user,text="Submit",fg="white",bg="#d77337",bd=0,font=("times new roman",20,"bold")).place(x=72,y=320,width=180)

            def quit():
                top.destroy()
                top.update()

            Back_button=Button(top,command=quit,text="Back to Home",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=72,y=380)

        Register_button=Button(Frame_login,command=create_registration,text="Register New Account",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=72,y=248)
        Login_button=Button(self.root,command=login_verify,text="Login",fg="white",bg="#d77337",bd=0,font=("times new roman",20,"bold")).place(x=310,y=460,width=180)
    
root = Tk()
app = Window(root)
root.mainloop()