
from tkinter import *
from tkinter import messagebox
import re

class EmployeeForm:

    def __init__(self, root):

        self.root = root
        self.root.title("Employee Registration")
        self.root.geometry("400x350")

        Label(root,text="Employee Registration Form",
              font=("Arial",14,"bold")).pack(pady=10)

        frame = Frame(root)
        frame.pack(pady=20)

        # Employee ID
        Label(frame,text="Employee ID").grid(row=0,column=0,padx=10,pady=5)
        self.emp_id = Entry(frame)
        self.emp_id.grid(row=0,column=1)

        # Employee Name
        Label(frame,text="Employee Name").grid(row=1,column=0,padx=10,pady=5)
        self.name = Entry(frame)
        self.name.grid(row=1,column=1)

        # Department
        Label(frame,text="Department").grid(row=2,column=0,padx=10,pady=5)
        self.dept = Entry(frame)
        self.dept.grid(row=2,column=1)

        # Salary
        Label(frame,text="Salary").grid(row=3,column=0,padx=10,pady=5)
        self.salary = Entry(frame)
        self.salary.grid(row=3,column=1)

        # Buttons
        Button(root,text="Add",width=12,command=self.validate).pack(pady=10)
        Button(root,text="Clear",width=12,command=self.clear).pack()

    # Validation
    def validate(self):

        empid = self.emp_id.get()
        name = self.name.get()
        dept = self.dept.get()
        salary = self.salary.get()

        if not re.match("^[0-9]+$", empid):
            messagebox.showerror("Error","Employee ID must be numbers")
            return

        if not re.match("^[A-Za-z ]+$", name):
            messagebox.showerror("Error","Name must contain only letters")
            return

        if not re.match("^[A-Za-z ]+$", dept):
            messagebox.showerror("Error","Department must contain letters")
            return

        if not re.match("^[0-9]+$", salary):
            messagebox.showerror("Error","Salary must be numbers")
            return

        messagebox.showinfo("Success","Employee Data Valid")

    # Clear fields
    def clear(self):
        self.emp_id.delete(0,END)
        self.name.delete(0,END)
        self.dept.delete(0,END)
        self.salary.delete(0,END)


root = Tk()
obj = EmployeeForm(root)
root.mainloop()