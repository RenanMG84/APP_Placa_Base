import tkinter as tk

def open_new_window():
    top = tk.Toplevel(root)
    top.title("Toplevel Window")
    label = tk.Label(top, text="This is a Toplevel window")
    label.pack()

    # Make the Toplevel window grab the focus and prevent interaction with the root window
    top.grab_set()

root = tk.Tk()
root.title("Main Window")

button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack()

root.mainloop()
