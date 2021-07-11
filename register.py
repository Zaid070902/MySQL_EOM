import mysql.connector
from tkinter import *

master = Tk()
master.config(bg="white")
master.geometry("500x500")
master.title("Login Page")

life = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='lifechoices'
                               , auth_plugin='mysql_native_password')
mycursor = life.cursor()
xy = mycursor.execute('SELECT * from register')

for i in mycursor:
    print(i)

user_lab = Label(master, text="Enter Name", bg="white", fg="red", font=100)
user_lab.place(x=50, y=50)
surname_lab = Label(master, text="Enter Surname", bg="white", fg="red", font=100)
surname_lab.place(x=50, y=100)
phone_lab = Label(master, text="Enter PhoneNumber", bg="white", fg="red", font=100)
phone_lab.place(x=50, y=150)
id_lab = Label(master, text="Enter ID Number", bg="white", fg="red", font=100)
id_lab.place(x=50, y=200)


user_ent = Entry(master, fg="white", bg="red", highlightbackground="red")
user_ent.place(x=250, y=50)
surname_ent = Entry(master, fg="white", bg="red", highlightbackground="red")
surname_ent.place(x=250, y=100)
phone_ent = Entry(master, fg="white", bg="red", highlightbackground="red")
phone_ent.place(x=250, y=150)
id_ent = Entry(master, fg="white", bg="red", highlightbackground="red")
id_ent.place(x=250, y=200)


def reg():
    x = "INSERT INTO register (Name, Surname, PhoneNumber, ID_number) VALUES (%s, %s, %s, %s)"
    y = (user_ent.get(), surname_ent.get(), phone_ent.get(), id_ent.get())
    mycursor.execute(x, y)

    life.commit()


register_btn = Button(master, text="Register new user", bg="white", highlightbackground="red", fg="red", command=reg)
register_btn.place(x=200, y=250)

master.mainloop()
