from tkinter import *
import tkinter.messagebox as mbox

def login():
    username = ent_username.get()
    password = ent_password.get()

    if username == "Admin" and password == "password":
        mbox.showinfo("Login result", "Successful Login")
    else:
        mbox.showinfo("Login result", "Incorrect credentials provided")

window = Tk()
window.title("Capture input with entry boxes")
window.geometry("700x100")

lbl_username = Label(window, text="Username:")
lbl_username.place(x=5, y=10)

ent_username = Entry(window)
ent_username.place(x=150, y=5)

lbl_password = Label(window, text="Password:")
lbl_password.place(x=5, y=40)

ent_password = Entry(window)
ent_password.place(x=150, y=45)

btn_login = Button(window, text="Login", command=login)
btn_login.place(x=380, y=65)

window.mainloop()
