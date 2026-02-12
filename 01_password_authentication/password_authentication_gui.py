import tkinter as tk
from tkinter import messagebox
import re

def check_password():
    password = entry_password.get()
    confirm_password = entry_confirm.get()

    if len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long")
        return

    if not re.search(r"[A-Z]", password):
        messagebox.showerror("Error", "Password must contain at least one uppercase letter")
        return

    if not re.search(r"[a-z]", password):
        messagebox.showerror("Error", "Password must contain at least one lowercase letter")
        return

    if not re.search(r"[0-9]", password):
        messagebox.showerror("Error", "Password must contain at least one digit")
        return

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        messagebox.showerror("Error", "Password must contain at least one special character")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    messagebox.showinfo("Success", "Password created successfully!\nAuthentication successful.")


root = tk.Tk()
root.title("Password Authentication System")
root.geometry("400x300")
root.resizable(False, False)


tk.Label(root, text="Create Password", font=("Arial", 12)).pack(pady=5)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack()

tk.Label(root, text="Confirm Password", font=("Arial", 12)).pack(pady=5)
entry_confirm = tk.Entry(root, show="*", width=30)
entry_confirm.pack()


tk.Button(root, text="Authenticate", command=check_password,
          bg="green", fg="white", width=15).pack(pady=20)

root.mainloop()