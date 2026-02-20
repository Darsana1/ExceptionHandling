from tkinter import *
app=Tk()
app.geometry('500x500')
app.title('Calculator')
# app.config(bg='lightgreen')
a=StringVar()
# def calc(num):
#         global n
#         n=entry.get()
#         n=n+str(num)
#         print(n)
#         a.set(n)

def calc(num):
        global current
        current=a.get()
        num_str=str(num)
        if num_str in '+-/%*//':
                if current and current[-1] in '+-/%*//':
                        a.set(current[:-1]+num_str)
                else:
                        a.set(current+num_str)
        else:
                if num_str.isdigit() and (current =='0' or current==''):
                        a.set(num_str)
                else:
                        a.set(current+num_str)

def eq1():
        exp=a.get()
        result=str(eval(exp))
        a.set(result)

def clr():
        a.set("")
def back():
        current=a.get()
        a.set(current[:-1])

#InputBox
entry = Entry(app, width=30, font=("Arial", 20), borderwidth=5, text=a,relief="ridge",bg="#333333", fg="white")
entry.pack(pady=20)
#Buttons

b1=Button(app,text='AC',font=('Arial',16,"bold"),fg='red',bg='blue',padx=20,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=clr)
b1.place(x=50,y=100)

b2=Button(app,text='//',font=('Arial',16,"bold"),fg='red',bg='lightblue',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc('//'))
b2.place(x=148,y=100)

b3=Button(app,text='%',font=('Arial',16,"bold"),bg='lightblue',fg='red',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc('%'))
b3.place(x=245,y=100)
b4=Button(app,text='/',font=('Arial',16,"bold"),bg='lightblue',fg='red',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc('/'))
b4.place(x=339,y=100)

#row2

b5=Button(app,text='7',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc(7))
b5.place(x=50,y=180)

b6=Button(app,text='8',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc(8))
b6.place(x=148,y=180)

b7=Button(app,text='9',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc(9))
b7.place(x=245,y=180)
b8=Button(app,text='*',font=('Arial',16,"bold"),bg='lightblue',fg='red',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc('*'))
b8.place(x=339,y=180)

#row3

# b5=Button(app,text='7',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2')
# b5.place(x=50,y=180)

# b6=Button(app,text='8',font=('Arial',16,"bold"),bg='darkgrey',padx=25,pady=10,borderwidth=5,relief='groove',cursor='hand2')
# b6.place(x=148,y=180)

# b7=Button(app,text='9',font=('Arial',16,"bold"),bg='darkgrey',padx=25,pady=10,borderwidth=5,relief='groove',cursor='hand2')
# b7.place(x=245,y=180)
# b8=Button(app,text='X',font=('Arial',16,"bold"),bg='darkgrey',padx=25,pady=10,borderwidth=5,relief='groove',cursor='hand2')
# b8.place(x=339,y=180)                

#row4
b9=Button(app,text='4',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc(4))
b9.place(x=50,y=260)
b10=Button(app,text='5',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc(5))
b10.place(x=148,y=260)
b11=Button(app,text='6',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc(6))
b11.place(x=245,y=260)
b12=Button(app,text='-',font=('Arial',16,"bold"),bg='lightblue',fg='red',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc('-'))
b12.place(x=339,y=260)

#row5

b13=Button(app,text='1',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc(1))
b13.place(x=50,y=340)
b14=Button(app,text='2',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc(2))
b14.place(x=148,y=340)
b15=Button(app,text='3',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc(3))
b15.place(x=245,y=340)
b16=Button(app,text='+',font=('Arial',16,"bold"),bg='lightblue',fg='red',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc('+'))
b16.place(x=339,y=340)

#row6

b17=Button(app,text='0',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=lambda:calc(0))
b17.place(x=50,y=420)
b18=Button(app,text='.',font=('Arial',16,"bold"),bg='darkgrey',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2')
b18.place(x=148,y=420)
b19=Button(app,text='X',font=('Arial',16,"bold"),bg='darkgrey',padx=23,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=back)
b19.place(x=245,y=420)
b20=Button(app,text='=',font=('Arial',16,"bold"),bg='lightblue',fg='green',padx=27,pady=10,borderwidth=5,relief='groove',cursor='hand2',command=eq1)
b20.place(x=339,y=420)
app.mainloop()
