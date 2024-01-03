import tkinter as tk

def get_nested_entry_value():
    # Access the Entry widget inside the nested frame
    nested_entry_value = nested_entry.get()
    print("Nested Entry value:", nested_entry_value)

root = tk.Tk()
root.title("Get Entry Value Inside Nested Frames")

# Create the outer frame
outer_frame = tk.Frame(root)
outer_frame.pack(padx=20, pady=20)

# Create a frame inside the outer frame
inner_frame = tk.Frame(outer_frame)
inner_frame.pack(padx=10, pady=10)

# Create an Entry widget inside the inner frame
nested_entry = tk.Entry(inner_frame)
nested_entry.pack(padx=5, pady=5)

# Create a button to get the value from the nested Entry widget
get_value_button = tk.Button(inner_frame, text="Get Nested Entry Value", command=get_nested_entry_value)
get_value_button.pack(padx=5, pady=5)

root.mainloop()
