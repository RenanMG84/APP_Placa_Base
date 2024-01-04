import tkinter as tk

class RadioButtonFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.radio_var = tk.StringVar()
        self.radio_var.set("Option 1")  # Set default value for the radio buttons

        # Create radio buttons
        self.radio_button1 = tk.Radiobutton(self, text="Option 1", variable=self.radio_var, value="Option 1")
        self.radio_button2 = tk.Radiobutton(self, text="Option 2", variable=self.radio_var, value="Option 2")
        self.radio_button3 = tk.Radiobutton(self, text="Option 3", variable=self.radio_var, value="Option 3")

        # Pack radio buttons
        self.radio_button1.pack(anchor=tk.W)
        self.radio_button2.pack(anchor=tk.W)
        self.radio_button3.pack(anchor=tk.W)

        # Display a button to show the selected option
        self.show_button = tk.Button(self, text="Show Selected", command=self.show_selected)
        self.show_button.pack(pady=10)

    def show_selected(self):
        selected_option = self.radio_var.get()
        print(f"Selected option: {selected_option}")

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Radio Button Example")

        radio_frame = RadioButtonFrame(self)
        radio_frame.pack(padx=20, pady=20)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
