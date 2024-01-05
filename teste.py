import tkinter as tk

def create_table(root, rows, columns):
    table_frame = tk.Frame(root)
    table_frame.pack()

    # Create headers
    for j in range(columns):
        header_label = tk.Label(table_frame, text=f"Header {j + 1}", relief=tk.RIDGE, width=15)
        header_label.grid(row=0, column=j)

    # Create initial rows and columns
    for i in range(1, rows + 1):
        for j in range(columns):
            cell_label = tk.Label(table_frame, text=f"Row {i}, Col {j + 1}", relief=tk.RIDGE, width=15)
            cell_label.grid(row=i, column=j)

    return table_frame  # Return the frame containing the table widgets

def add_row(frame, columns):
    # Get the number of rows in the table
    rows = len(frame.grid_slaves()) // columns

    # Create a new row
    for j in range(columns):
        cell_label = tk.Label(frame, text=f"Row {rows + 1}, Col {j + 1}", relief=tk.RIDGE, width=15)
        cell_label.grid(row=rows + 1, column=j)

def remove_row(frame):
    children = frame.grid_slaves()
    if children:
        last_row = max(child.grid_info()["row"] for child in children)
        for child in children:
            if child.grid_info()["row"] == last_row:
                child.grid_forget()
                child.destroy()

root = tk.Tk()
root.title("Table Example")

num_rows = 5
num_columns = 3

table_frame = create_table(root, num_rows, num_columns)

add_button = tk.Button(root, text="Add Row", command=lambda: add_row(table_frame, num_columns))
add_button.pack()

remove_button = tk.Button(root, text="Remove Row", command=lambda: remove_row(table_frame))
remove_button.pack()

root.mainloop()
