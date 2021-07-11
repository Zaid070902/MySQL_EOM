import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

master3 = Tk()
master3.config(bg="white")
master3.geometry("500x500")
master3.title("Login Page")

Password_lab = Label(master3, text="Enter Admin Password", fg="red", bg="white", font=200)
Password_lab.place(x=160, y=100)
Password_ent = Entry(master3, fg="white", bg="red", highlightbackground="red", border=1, width=22)
Password_ent.place(x=160, y=170)


def adlog():
    if Password_ent.get() == "8-2fermENt2020":
        messagebox.showinfo("Admin", "Access Granted")
        master3.destroy()
        import admin2
    else:
        messagebox.showinfo("Admin", "Access denied")


adminLog_btn = Button(master3, text="login", bg="white", highlightbackground="red", fg="red", width=19, command=adlog)
adminLog_btn.place(x=160, y=240)

master3.mainloop()
