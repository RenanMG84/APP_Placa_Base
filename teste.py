import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Scrollbar in Frame")

# Create a canvas and add a scrollbar to it
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Create a frame to contain the scrollable content
frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Function to configure the canvas scrolling region
def configure_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", configure_scroll_region)

# Configure the canvas scrolling
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)

# Adding widgets to the scrollable frame
for i in range(50):
    ttk.Label(frame, text=f"Label {i}").pack()

root.mainloop()
