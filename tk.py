from tkinter import *

top = Tk()
top.geometry("200x200")
top.title("Registation Form")
name = Label(top, text="Registation Form", width=20,font=("bold", 20)).place(x=5, y=10)
name = Label(top, text="Sr_No").place(x=30, y=50)
name = Label(top, text="Name").place(x=30, y=90)
name = Label(top, text="Roll NO").place(x=30, y=133)
name = Label(top, text="Address").place(x=30, y=180)
name = Label(top, text="Branch").place(x=30, y=230)
list_of_Branch = ['CS', 'IT', 'ECE', 'CIVIL']
c = StringVar()
droplist = OptionMenu(top, c, *list_of_Branch)
droplist.config(width=15)
c.set('Select your Branch')
droplist.place(x=100, y=230)

name = Label(top, text="Gender").place(x=30, y=260)
var = IntVar()
Radiobutton(top, text="Male", padx=5, variable=var, value=1).place(x=90, y=260)
Radiobutton(top, text="Female", padx=20, variable=var, value=2).place(x=170, y=260)

e1 = Entry(top).place(x=80, y=50)
e2 = Entry(top).place(x=80, y=90)
e3 = Entry(top).place(x=80, y=133)
e4 = Entry(top).place(x=80, y=180)

Button(top, text='Submit' , width=20,bg="red",fg='white').place(x=100,y=380)


top.mainloop()
