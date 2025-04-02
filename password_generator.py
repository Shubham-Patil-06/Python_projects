import random
import string
import tkinter as tk
from tkinter import messagebox

# Ensure Tkinter is installed
# Tkinter is included by default with Python on Windows and macOS.
# On Linux, you may need to install it using:
# sudo apt-get install python3-tk (Debian/Ubuntu)
# sudo pacman -S tk (Arch Linux)
# sudo dnf install python3-tkinter (Fedora)

def generate_password():
    length = int(length_entry.get())
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()
    
    characters = string.ascii_letters  # Uppercase and lowercase letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Widgets
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

digits_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=True)

chk_digits = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
chk_digits.pack()
chk_special_chars = tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var)
chk_special_chars.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, state='readonly', width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

# Run the application
root.mainloop()
