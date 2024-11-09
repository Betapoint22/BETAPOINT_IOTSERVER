import tkinter as tk

def submit():
    print("Name:", name_entry.get())
    print("Email:", email_entry.get())

# Create the main window
window = tk.Tk()
window.title("Simple Form")

# Create labels and entry fields
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

# Create a submit button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

# Start the event loop
window.mainloop()