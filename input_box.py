import tkinter as tk


class InputBox:
    def __init__(self, entry_list):
        self.root = tk.Tk()
        self.root.title("Edge creator")
        self.root.geometry("230x130")
        self.return_list = entry_list
        self.label1 = tk.Label(self.root, text="source:")
        self.label1.grid(column=1, row=0, padx=3, pady=3)
        self.entry_s = tk.Entry(self.root)
        self.entry_s.grid(column=2, row=0, padx=3, pady=3)
        self.label2 = tk.Label(self.root, text="destination:")
        self.label2.grid(column=1, row=1, padx=3, pady=3)
        self.entry_d = tk.Entry(self.root)
        self.entry_d.grid(column=2, row=1, padx=3, pady=3)
        self.label3 = tk.Label(self.root, text="weight:")
        self.label3.grid(column=1, row=2, padx=3, pady=3)
        self.entry_w = tk.Entry(self.root)
        self.entry_w.grid(column=2, row=2, padx=3, pady=3)
        self.button = tk.Button(self.root, text="OK", command=self.submit_value)
        self.button.grid(column=2, row=3, padx=3, pady=3)

    def submit_value(self):
        value1 = self.entry_s.get()
        value2 = self.entry_d.get()
        value3 = self.entry_w.get()
        self.return_list.append(value1)
        self.return_list.append(value2)
        self.return_list.append(value3)
        self.root.destroy()

    def run(self):
        self.root.mainloop()
