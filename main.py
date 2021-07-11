import mysql.connector
from tkinter import *
from tkinter import messagebox

root = Tk()
root.config(bg="white")
root.geometry("500x500")
root.title("Login Page")


def admin():
    root.destroy()
    import admin


admin_btn = Button(root, text="Admin", bg="white", highlightbackground="red", fg="red", width=20, command=admin)
admin_btn.place(x=170, y=50)


def log():
    root.destroy()
    import login


log_btn = Button(root, text="Login", bg="white", highlightbackground="red", fg="red", command=log, width=20)
log_btn.place(x=170, y=150)


def reg():
    root.destroy()
    import register


register_btn = Button(root, text="Register new user", bg="white", highlightbackground="red", fg="red", command=reg, width=20)
register_btn.place(x=170, y=250)


root.mainloop()
