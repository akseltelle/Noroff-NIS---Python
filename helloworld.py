from tkinter import *

window = Tk()

window.title("Hello World")

window.geometry("700x400")

label = Label(window, text="Hello World!")

label.pack(padx=200, pady=50)

window.mainloop()
