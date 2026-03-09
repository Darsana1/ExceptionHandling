# from tkinter import *

# app= Tk()
# app.geometry('500x500')
# app.title('Registration Form')
# #heading

# Label(app, text="Registration Form",fg='red', font=("Arial", 18, "bold")).pack(pady=10)


# f1=Frame(app,highlightbackground='blue',highlightthickness='3',width=400,height=250,bd=2,relief="ridge")
# f1.pack(padx=20, pady=10, fill="both", expand=True)


# lb1=Label(f1,text='FIRST NAME',padx=15, bd=2, relief="ridge",width=10)
# lb1.place(x=20,y=20)

# #entry box-single line text
# en1=Entry(f1,width=30)
# en1.place(x=140,y=20)

# lb2=Label(f1,text='LAST NAME',padx=15, bd=2, relief="ridge",width=10)
# lb2.place(x=20,y=50)

# #entry box-single line text
# en2=Entry(f1,width=30)
# en2.place(x=140,y=50)

# lb3=Label(f1,text='PHONE NO',padx=15, bd=2, relief="ridge",width=10)
# lb3.place(x=20,y=80)

# #entry box-single line text
# en3=Entry(f1,width=30)
# en3.place(x=140,y=80)

# lb4=Label(f1,text='EMAIL',padx=15, bd=2, relief="ridge",width=10)
# lb4.place(x=20,y=110)

# #entry box-single line text
# en4=Entry(f1,width=30)
# en4.place(x=140,y=110)

# lb5=Label(f1,text='AGE',padx=15, bd=2, relief="ridge",width=10)
# lb5.place(x=20,y=140)

# age_var = IntVar()
# age_var.set(20)   # default value

# sp=Spinbox(app,textvariable=age_var,from_=1,to=120)
# sp.place(x=166,y=210,width=80)

# # gender
# Label(f1, text="Gender:",padx=15, bd=2, relief="ridge",width=10).place(x=20,y=170)

# gender = StringVar()
# Radiobutton(f1, text="Male", variable=gender, value="Male", bg="white").place(x=140,y=170)
# Radiobutton(f1, text="Female", variable=gender, value="Female", bg="white").place(x=200,y=170)


# lb1=Label(f1,text='PASSWORD',padx=15, bd=2, relief="ridge",width=10)
# lb1.place(x=20,y=200)

# #entry box-single line text
# en1=Entry(f1,width=30)
# en1.place(x=140,y=200)
# lb1=Label(f1,text='CONFIRM PSWD',padx=15, bd=2, relief="ridge",width=10)
# lb1.place(x=20,y=240)

# #entry box-single line text
# en1=Entry(f1,width=30)
# en1.place(x=140,y=240)



# def valiadtion_check():
#         fname=lb1
#         lname=lb2



# # submit button
# Button(app, text="Register", font=("Arial", 12, "bold"),
#        bg="#4CAF50", fg="white", width=15).pack(pady=20)
# app.mainloop()

from tkinter import *
import re
from tkinter import messagebox

app= Tk()
app.geometry('500x500')
app.title('Registration Form')

Label(app, text="Registration Form",fg='red', font=("Arial", 18, "bold")).pack(pady=10)

f1=Frame(app,highlightbackground='blue',bg='lightpink',highlightthickness='3',
         width=400,height=250,bd=2,relief="ridge")
f1.pack(padx=20, pady=10, fill="both", expand=True)

# FIRST NAME
Label(f1,text='FIRST NAME',padx=15, bd=2, relief="ridge",width=10).place(x=20,y=20)
fname=Entry(f1,width=30)
fname.place(x=140,y=20)

# LAST NAME
Label(f1,text='LAST NAME',padx=15, bd=2, relief="ridge",width=10).place(x=20,y=50)
lname=Entry(f1,width=30)
lname.place(x=140,y=50)

# PHONE
Label(f1,text='PHONE NO',padx=15, bd=2, relief="ridge",width=10).place(x=20,y=80)
phone=Entry(f1,width=30)
phone.place(x=140,y=80)

# EMAIL
Label(f1,text='EMAIL',padx=15, bd=2, relief="ridge",width=10).place(x=20,y=110)
email=Entry(f1,width=30)
email.place(x=140,y=110)

# AGE
Label(f1,text='AGE',padx=15, bd=2, relief="ridge",width=10).place(x=20,y=140)
age_var = IntVar()
age_var.set(20)
Spinbox(f1,textvariable=age_var,from_=1,to=120,width=28).place(x=140,y=140)

# GENDER
Label(f1, text="Gender",padx=15, bd=2, relief="ridge",width=10).place(x=20,y=170)
gender = StringVar()
Radiobutton(f1, text="Male", variable=gender, value="Male").place(x=140,y=170)
Radiobutton(f1, text="Female", variable=gender, value="Female").place(x=200,y=170)

# PASSWORD
Label(f1,text='PASSWORD',padx=15, bd=2, relief="ridge",width=10).place(x=20,y=200)
password=Entry(f1,width=30,show="*")
password.place(x=140,y=200)

# CONFIRM PASSWORD
Label(f1,text='CONFIRM PSWD',padx=15, bd=2, relief="ridge",width=10).place(x=20,y=240)
cpassword=Entry(f1,width=30,show="*")
cpassword.place(x=140,y=240)

# VALIDATION FUNCTION
def validate():

    fname_val = fname.get()
    lname_val = lname.get()
    phone_val = phone.get()
    email_val = email.get()
    pass_val = password.get()
    cpass_val = cpassword.get()

    # name validation
    if not re.match("^[A-Za-z]+$", fname_val):
        messagebox.showerror("Error","Invalid First Name")
        return

    if not re.match("^[A-Za-z]+$", lname_val):
        messagebox.showerror("Error","Invalid Last Name")
        return

    # phone validation
    if not re.match("^[0-9]{10}$", phone_val):
        messagebox.showerror("Error","Phone must be 10 digits")
        return

    # email validation
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email_val):
        messagebox.showerror("Error","Invalid Email")
        return

    # password validation
    if len(pass_val) < 6:
        messagebox.showerror("Error","Password must be at least 6 characters")
        return

    if pass_val != cpass_val:
        messagebox.showerror("Error","Passwords do not match")
        return

    messagebox.showinfo("Success","Registration Successful")

# SUBMIT BUTTON
Button(app, text="Register",
       command=validate,
       font=("Arial", 12, "bold"),
       bg="#4CAF50", fg="white",
       width=15).pack(pady=20)

app.mainloop()