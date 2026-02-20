from tkinter import *

app= Tk()
app.geometry('500x500')
app.title('Registration Form')


f1=Frame(app,highlightbackground='blue',highlightthickness='3',bg='lightgreen',width=400,height=500)
f1.place(x=50,y=40)


lb1=Label(f1,text='FIRST NAME',padx=15)
lb1.place(x=20,y=20)

#entry box-single line text
en1=Entry(f1)
en1.place(x=140,y=20)

app.mainloop()