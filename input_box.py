import tkinter as tk


class InputBox(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Helper")
        self.geometry('500x763')

    def run(self):
        self.mainloop()