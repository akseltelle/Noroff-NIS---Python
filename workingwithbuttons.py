from tkinter import *

def update_colour():
    if window.cget("bg") == "lightgrey":
        window.configure(bg="red")
    else:
        window.configure(bg="lightgrey")

window = Tk()
window.title("Working with buttons")
window.geometry("700x400")

window.configure(bg="lightgrey")

btn_update = Button(window, text="Update colour", command=update_colour)
btn_update.place(x=20, y=20)
btn_exit = Button(window, text="Exit", command=exit)
btn_exit.place(x=120, y=20)
window.mainloop()
