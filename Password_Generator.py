import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Weak Password", "Password length should be at least 4.")
            return
        
        characters = ""
        if var_letters.get():
            characters += string.ascii_letters
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation
        
        if not characters:
            messagebox.showerror("Error", "Please select at least one option (letters, digits, symbols).")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter password length:", font=("Arial", 12)).pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack()

var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=var_letters, font=("Arial", 10)).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Digits", variable=var_digits, font=("Arial", 10)).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols, font=("Arial", 10)).pack(anchor="w", padx=50)

tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="green", fg="white").pack(pady=15)

tk.Label(root, text="Generated Password:", font=("Arial", 12)).pack()
result_entry = tk.Entry(root, font=("Arial", 12), justify="center")
result_entry.pack(pady=5)

root.mainloop()
