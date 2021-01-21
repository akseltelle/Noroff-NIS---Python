from tkinter import *

def calculate():
    total = 0
    total += topping_1.get()
    total += topping_2.get()
    total += topping_3.get()
    calculation.set("Total cost=\t{}.".format(total))

window = Tk()
window.title("Calculating a sandwich price with checkbuttons")
window.geometry("700x140")

frame_toppings = Frame(window)
frame_toppings.place(x=10, y=10)

topping_1 = IntVar()
topping_2 = IntVar()
topping_3 = IntVar()

chk_cheese = Checkbutton(frame_toppings, onvalue=5, offvalue=0,
                         text="Cheese", variable=topping_1, command=calculate)
chk_cheese.pack(side=TOP, anchor=W)
chk_ham = Checkbutton(frame_toppings, onvalue=10, offvalue=0,
                         text="Ham", variable=topping_2, command=calculate)
chk_ham.pack(side=TOP, anchor=W)
chk_tomato = Checkbutton(frame_toppings, onvalue=3, offvalue=0,
                         text="Tomato", variable=topping_3, command=calculate)
chk_tomato.pack(side=TOP, anchor=W)

calculation = StringVar()
calculate()
lbl_calculation = Label(frame_toppings, textvariable=calculation)
lbl_calculation.pack(anchor=W, pady=10)

window.mainloop()
