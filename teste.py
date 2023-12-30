import tkinter as tk

def toggle_button_state():
    if check_var.get() == 1:  # If the checkbox is checked
        button.config(state=tk.NORMAL)  # Enable the button
    else:
        button.config(state=tk.DISABLED)  # Disable the button

root = tk.Tk()
root.title("Checkbox and Button Example")

# Variable to hold the state of the checkbox
check_var = tk.IntVar()

# Create a checkbox
checkbox = tk.Checkbutton(root, text="Enable Button", variable=check_var, command=toggle_button_state)
checkbox.pack(padx=10, pady=10)

# Create a button initially disabled
button = tk.Entry(root, state=tk.DISABLED)
button.pack(padx=10, pady=10)

root.mainloop()
