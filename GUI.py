import tkinter as tk

# Create window
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("400x250")

# Heading
title = tk.Label(root, text="GUI Development Task", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Name Label
name_label = tk.Label(root, text="Enter Your Name:")
name_label.pack()

# Entry Box
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Function for button
def submit():
    name = name_entry.get()
    if name:
        result_label.config(text=f"Hello, {name}!")
    else:
        result_label.config(text="Please enter your name.")

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run application
root.mainloop()
