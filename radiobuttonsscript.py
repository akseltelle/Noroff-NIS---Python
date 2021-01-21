from tkinter import *

def show_options():
    options.set("{} aged {}.".format(gender.get(), agerange.get()))

window = Tk()
window.title("Providing options with radiobuttons")
window.geometry("700x140")

frame_gender = Frame(window, bg="lightgray")
frame_gender.place(x=10, y=10)
frame_agerange = Frame(window, bg="lightgray")
frame_agerange.place(x=120, y=10)

btn_select = Button(window, text="Select", command=show_options)
btn_select.place(x=10, y=80)
gender = StringVar()

rad_female = Radiobutton(frame_gender, text="Female", value="Female", variable=gender, bg="lightgray")
rad_female.pack(side=TOP, anchor=W)
rad_male = Radiobutton(frame_gender, text="Male", value="Male", variable=gender, bg="lightgray")
rad_male.pack(side=TOP, anchor=W)
rad_female.select()
agerange = StringVar()

rad_under18 = Radiobutton(frame_agerange, text="Under 18", value="under 18", variable=agerange, bg="lightgray")
rad_under18.pack(side=TOP, anchor=W)
rad_18to30 = Radiobutton(frame_agerange, text="18 to 30", value="18 to 30", variable=agerange, bg="lightgray")
rad_18to30.pack(side=TOP, anchor=W)
rad_over30 = Radiobutton(frame_agerange, text="Over 30", value="over 30", variable=agerange, bg="lightgray")
rad_over30.pack(side=TOP, anchor=W)
rad_18to30.select()

options = StringVar()
show_options()

lbl_options = Label(window, textvariable=options)
lbl_options.place(x=10, y=110)
window.mainloop()