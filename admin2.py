import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

master4 = Tk()
master4.config(bg="white")
master4.geometry("500x500")
master4.title("Login Page")

life = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='lifechoices'
                               , auth_plugin='mysql_native_password')
# mycursor = life.cursor()
# xy = mycursor.execute('SELECT * from login')


def log_table():
    master4.config(bg="red")
    log_table_btn.config(bg="red", fg="white")

    dead = life.cursor()
    dead.execute("SELECT * FROM login limit 0,10")
    i = 0
    for student in dead:
        for j in range(len(student)):
            e = Entry(master4, width=10, fg='white', bg="red", highlightbackground="red", border=1)
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i+1


log_table_btn = Button(master4, text="Display Login", command=log_table,  bg="white", highlightbackground="red", fg="red")
log_table_btn.place(x=50, y=200)


def reg_table():
    master4.config(bg="blue")
    reg_table_btn.config(bg="blue", fg="white")

    dead = life.cursor()
    dead.execute("SELECT * FROM register limit 0,10")
    i = 0
    for student in dead:
        for j in range(len(student)):
            e = Entry(master4, width=10, fg='white', bg="blue", highlightbackground="blue", border=1)
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i+1


reg_table_btn = Button(master4, text="Display Register", command=reg_table,  bg="white", highlightbackground="blue", fg="blue")
reg_table_btn.place(x=250, y=200)


master4.mainloop()
