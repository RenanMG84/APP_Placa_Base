from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tk test")
root.geometry("800x800")

frame_1 = ttk.Frame(root, relief="sunken", height="400", width="400").grid(row=0, column=0, rowspan=1, columnspan=1)
frame_2 = ttk.Frame(frame_1, relief="sunken", height="200", width="200").grid(row=0, column=0, rowspan=1, columnspan=1)
label_1 = ttk.Label(frame_2, text="Text").grid(row=0, column=0, sticky="N, E")

root.mainloop()