from tkinter import *

def show_selection():
    message.set("Index:\t{}\nValue:\t{}".format(listbox.curselection(),
                                                listbox.get(listbox.curselection())))

window = Tk()
window.title("Options in a listbox")
window.geometry("700x250")

frame = Frame(window)

frame.pack(side=TOP, pady=10)

listbox = Listbox(frame, width=40)

listbox.insert(1, "LAW061 - Security and the Law")
listbox.insert(2, "SEC061 - Network Security")
listbox.insert(3, "RAS061 - Preventive Security")
listbox.insert(END, "HIR071 - Hacking Tools, Incidents and Response")
listbox.insert(5, "PRG111 - Programming")
listbox.insert(6, "SQL051 - Databases")
listbox.insert(END, "COF061 - Computer Forensics")
listbox.pack(side=LEFT, padx=5)

btn = Button(frame, text="Select", command=show_selection)
btn.pack(side=RIGHT)

message = StringVar()
message.set("No selection made")
lbl_selected = Label(window, textvariable=message)
lbl_selected.pack(side=BOTTOM, pady=10)

window.mainloop()
