import tkinter as tk
from tkinter import messagebox
import getpass  # For password input without echo

# In-memory storage for feedback
feedback_list = []

# Function to submit feedback
def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    feedback = feedback_entry.get("1.0", tk.END)

    if name and email and feedback.strip():
        feedback_list.append({
            'name': name,
            'email': email,
            'feedback': feedback.strip()
        })
        messagebox.showinfo("Success", "Feedback submitted successfully!")
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        feedback_entry.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")

# Function to print current feedback
def print_data():
    password = getpass.getpass("Enter password to view feedback: ")  # Password prompt in the console
    if password == "your_password":  # Replace with your chosen password
        print("\nCurrent Feedback Records:")
        if feedback_list:
            for record in feedback_list:
                print(record)
        else:
            print("No feedback available.")
    else:
        print("Access Denied: Incorrect password!")

# Create the main window
root = tk.Tk()
root.title("Customer Feedback Form")

# Create input fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Feedback").pack()
feedback_entry = tk.Text(root, height=5, width=30)
feedback_entry.pack()

# Create buttons
submit_button = tk.Button(root, text="Submit Feedback", command=submit_feedback)
submit_button.pack()

print_button = tk.Button(root, text="Print Feedback", command=print_data)
print_button.pack()

# Run the application
root.mainloop()
