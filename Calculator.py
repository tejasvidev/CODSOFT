import tkinter as tk
from tkinter import messagebox

LIGHT_THEME = {
    "bg": "#f5f5f5",
    "entry_bg": "white",
    "entry_fg": "black",
    "btn_bg": "#e0e0e0",
    "btn_fg": "black",
    "op_bg": "#2196F3",
    "op_fg": "white"
}

DARK_THEME = {
    "bg": "#121212",
    "entry_bg": "#1e1e1e",
    "entry_fg": "white",
    "btn_bg": "#333333",
    "btn_fg": "white",
    "op_bg": "#00bcd4",
    "op_fg": "black"
}

theme = LIGHT_THEME  

def apply_theme():
    root.config(bg=theme["bg"])
    entry.config(bg=theme["entry_bg"], fg=theme["entry_fg"])
    history_label.config(bg=theme["bg"], fg=theme["entry_fg"])
    for b in buttons:
        if b["text"] in "+-*/=":
            b.config(bg=theme["op_bg"], fg=theme["op_fg"])
        else:
            b.config(bg=theme["btn_bg"], fg=theme["btn_fg"])
    clear_btn.config(bg="#f44336", fg="white")
    back_btn.config(bg="#9C27B0", fg="white")
    theme_menu.config(bg="#607D8B", fg="white")

def click(btn_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + btn_text)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        update_history(expression + " = " + str(result))
    except:
        messagebox.showerror("Error", "Invalid Input")

def update_history(record):
    history_list.insert(0, record)
    if history_list.size() > 5:
        history_list.delete(5, tk.END)

def key_press(event):
    char = event.char
    if char.isdigit() or char in "+-*/.":
        click(char)
    elif char == "\r":
        calculate()
    elif char == "\x08":
        backspace()
    return "break"

def change_theme(option):
    global theme
    theme = LIGHT_THEME if option == "Light" else DARK_THEME
    apply_theme()

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("400x600")
root.resizable(False, False)

entry = tk.Entry(root, font=("Segoe UI", 22), relief="solid", bd=2, justify="right")
entry.pack(pady=15, padx=10, fill="x")

history_label = tk.Label(root, text="History (last 5):", font=("Segoe UI", 12, "bold"))
history_label.pack(pady=5)

history_list = tk.Listbox(root, height=5, font=("Segoe UI", 10), bd=0, highlightthickness=0)
history_list.pack(padx=10, pady=5, fill="x")

btn_frame = tk.Frame(root)
theme_var = tk.StringVar(value="Light")
theme_menu = tk.OptionMenu(root, theme_var, "Light", "Dark", command=change_theme)
theme_menu.config(width=15, font=("Segoe UI", 12))
theme_menu.pack(pady=10)
btn_frame.pack(padx=10, pady=10)

buttons = []
btn_layout = [
    ("7",0,0), ("8",0,1), ("9",0,2), ("/",0,3),
    ("4",1,0), ("5",1,1), ("6",1,2), ("*",1,3),
    ("1",2,0), ("2",2,1), ("3",2,2), ("-",2,3),
    ("0",3,0), (".",3,1), ("=",3,2), ("+",3,3),
]

for (text, row, col) in btn_layout:
    if text == "=":
        cmd = calculate
    else:
        cmd = lambda x=text: click(x)
    b = tk.Button(btn_frame, text=text, width=6, height=2,
                  font=("Segoe UI", 16, "bold"), relief="flat",
                  command=cmd)
    b.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    buttons.append(b)

clear_btn = tk.Button(root, text="Clear", width=15, height=2,
                      font=("Segoe UI", 12, "bold"), relief="flat",
                      command=clear)
clear_btn.pack(pady=5)

back_btn = tk.Button(root, text="⌫ Backspace", width=15, height=2,
                     font=("Segoe UI", 12, "bold"), relief="flat",
                     command=backspace)
back_btn.pack(pady=5)

theme_var = tk.StringVar(value="Light")
theme_menu = tk.OptionMenu(root, theme_var, "Light", "Dark", command=change_theme)
theme_menu.config(width=15, font=("Segoe UI", 12))
theme_menu.pack(pady=5)

root.bind("<Key>", key_press)
apply_theme()
root.mainloop()
