import tkinter as tk
from tkinter import messagebox

# Colors and fonts
BG_COLOR = "#F5F7FA"
GRADIENT_TOP = "#89F7FE"
GRADIENT_BOTTOM = "#66A6FF"
BUTTON_COLOR = "#4A90E2"
FONT = ("Segoe UI", 12)

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x500")
root.config(bg=BG_COLOR)
root.resizable(False, False)

# Create a canvas for gradient effect
canvas = tk.Canvas(root, width=400, height=200, highlightthickness=0)
canvas.pack()
for i in range(256):
    r = int(137 + (102 - 137) * (i / 255))
    g = int(247 + (166 - 247) * (i / 255))
    b = int(254 + (255 - 254) * (i / 255))
    color = f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_line(0, i, 400, i, fill=color)

# Title
title_label = tk.Label(root, text="Welcome Back!", font=("Segoe UI", 20, "bold"), bg=BG_COLOR, fg="#333")
title_label.pack(pady=(10, 5))

subtitle_label = tk.Label(root, text="Please login to continue", font=("Segoe UI", 12), bg=BG_COLOR, fg="#666")
subtitle_label.pack(pady=(0, 20))

# Login frame
login_frame = tk.Frame(root, bg=BG_COLOR)
login_frame.pack(pady=10)

# Username
tk.Label(login_frame, text="Username", font=FONT, bg=BG_COLOR).grid(row=0, column=0, sticky="w", pady=(0, 5))
username_entry = tk.Entry(login_frame, font=FONT, width=30, bd=2, relief="groove")
username_entry.grid(row=1, column=0, pady=(0, 15))

# Password
tk.Label(login_frame, text="Password", font=FONT, bg=BG_COLOR).grid(row=2, column=0, sticky="w", pady=(0, 5))
password_entry = tk.Entry(login_frame, font=FONT, width=30, bd=2, relief="groove", show="*")
password_entry.grid(row=3, column=0, pady=(0, 20))

# Login Button
login_btn = tk.Button(root, text="Login", font=("Segoe UI", 12, "bold"), bg=BUTTON_COLOR, fg="white",
                      activebackground="#357ABD", activeforeground="white", width=20, height=2, command=login)
login_btn.pack(pady=10)

# Footer
footer = tk.Label(root, text="Forgot password?", font=("Segoe UI", 10), bg=BG_COLOR, fg="#888")
footer.pack(pady=(5, 0))

# Run app
root.mainloop()

