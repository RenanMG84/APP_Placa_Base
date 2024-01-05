import tkinter as tk

root = tk.Tk()
root.title("Special Characters in Tkinter")

# Using Unicode characters directly in strings
label_unicode = tk.Label(root, text="Unicode Characters: \u00A9 \u03A9 \u2665")
label_unicode.pack()

# Using ASCII codes (using chr() function)
label_ascii = tk.Label(root, text="ASCII Characters: " + chr(951) + " " + chr(2340) + " " + chr(9829))
label_ascii.pack()

root.mainloop()
