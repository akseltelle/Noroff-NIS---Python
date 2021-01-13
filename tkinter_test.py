# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello Friend\n(click me)"
        self.hi_there["command"] = self.hello_friend
        self.hi_there.pack(side="top")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "whoami?\n(click me)"
        self.hi_there["command"] = self.whoami
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    def hello_friend(self):
        print("hi there, friend!")
    def whoami(self):
        print("You are ROOT!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
