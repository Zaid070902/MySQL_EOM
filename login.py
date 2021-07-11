import mysql.connector
from tkinter import *
from tkinter import messagebox

master2 = Tk()
master2.config(bg="white")
master2.geometry("500x500")
master2.title("Login Page")

user_lab = Label(master2, text="Enter Name", bg="white", fg="red", font=100)
user_lab.place(x=50, y=50)
surname_lab = Label(master2, text="Enter Last Name", bg="white", fg="red", font=100)
surname_lab.place(x=50, y=100)

user_ent = Entry(master2, fg="red", highlightbackground="red")
user_ent.place(x=250, y=50)
surname_ent = Entry(master2, fg="red", highlightbackground="red")
surname_ent.place(x=250, y=100)


def log():
    life = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                   database='lifechoices'
                                   , auth_plugin='mysql_native_password')
    mycursor = life.cursor(buffered=True)
    xy = mycursor.execute('SELECT * from register')

    for curse in mycursor:
        if user_ent.get() == curse[0] and surname_ent.get() == curse[1]:
            messagebox.showinfo("", "Login Successful! Enjoy Your Day")
            log_code = "INSERT INTO login (name, surname) VALUES (%s, %s)"
            entry_values = (user_ent.get(), surname_ent.get())
            master2.destroy()
            mycursor.execute(log_code, entry_values)
            break
    else:
        messagebox.showinfo("", "Login Unsuccessful.")


log_btn = Button(master2, text="Login", bg="white", highlightbackground="red", fg="red", command=log)
log_btn.place(x=50, y=250)


master2.mainloop()
