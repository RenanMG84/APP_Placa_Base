import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Main Window")
        self.geometry("300x200")

        self.var_from_toplevel = tk.StringVar()
        self.label = tk.Label(self, textvariable=self.var_from_toplevel)
        self.label.pack()

        self.open_toplevel_button = tk.Button(self, text="Open Toplevel", command=self.open_toplevel)
        self.open_toplevel_button.pack()

    def open_toplevel(self):
        toplevel = ToplevelWindow(self)

    def update_variable(self, new_value):
        self.var_from_toplevel.set(new_value)

class ToplevelWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Toplevel Window")

        self.label = tk.Label(self, text="Enter value:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.pass_value_button = tk.Button(self, text="Pass Value", command=self.pass_value)
        self.pass_value_button.pack()

    def pass_value(self):
        value_to_pass = self.entry.get()
        self.master.update_variable(value_to_pass)
        self.destroy()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
