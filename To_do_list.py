import tkinter as tk
from tkinter import messagebox
import json, os

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x550")
root.config(bg="#f5f5f5")

tasks = []
fn = "tasks.json"

FONT_MAIN = ("Segoe UI", 12)
BTN_COLOR = "#4CAF50"
BTN_TEXT = "white"

frame_tasks = tk.Frame(root, bg="#f5f5f5")
frame_tasks.pack(pady=20)

scrollbar = tk.Scrollbar(frame_tasks)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_list = tk.Listbox(
    frame_tasks,
    width=40,
    height=15,
    font=FONT_MAIN,
    selectmode=tk.SINGLE,
    yscrollcommand=scrollbar.set,
    bd=0,
    highlightthickness=0,
    selectbackground="#a0d8ef",
    activestyle="none"
)
task_list.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=task_list.yview)

t_entry = tk.Entry(root, width=30, font=FONT_MAIN, relief="solid", bd=1)
t_entry.pack(pady=10)

def add_task():
    task = t_entry.get().strip()
    if task != "":
        tasks.append(task)
        task_list.insert(tk.END, task)
        t_entry.delete(0, tk.END)

def del_task():
    try:
        sel = task_list.curselection()[0]
        task_list.delete(sel)
        tasks.pop(sel)
    except:
        pass

def clr_task():
    tasks.clear()
    task_list.delete(0, tk.END)

def edit_task():
    try:
        s = task_list.curselection()[0]
        n_txt = t_entry.get().strip()
        if n_txt != "":
            tasks[s] = n_txt
            task_list.delete(s)
            task_list.insert(s, n_txt)
            t_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to edit")

def save_task():
    with open(fn, "w") as f:
        json.dump(tasks, f)

def load_task():
    global tasks
    if os.path.exists(fn):
        with open(fn, "r") as f:
            tasks = json.load(f)
            for task in tasks:
                task_list.insert(tk.END, task)


def close():
    if messagebox.askyesno("Quit", "Are you sure you want to close this application?"):
        save_task()
        root.destroy()

btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=15)

def styled_button(master, text, cmd, color=BTN_COLOR):
    return tk.Button(
        master, text=text, command=cmd,
        font=("Segoe UI", 10, "bold"),
        bg=color, fg=BTN_TEXT,
        activebackground="#388E3C",
        activeforeground="white",
        relief="flat", padx=15, pady=5,
        bd=0
    )

add_bn = styled_button(btn_frame, "Add", add_task)
add_bn.grid(row=0, column=0, padx=5)

edit_bn = styled_button(btn_frame, "Update", edit_task, "#2196F3")
edit_bn.grid(row=0, column=1, padx=5)

del_bn = styled_button(btn_frame, "Delete", del_task, "#f44336")
del_bn.grid(row=0, column=2, padx=5)

clr_bn = styled_button(btn_frame, "Clear All", clr_task, "#9C27B0")
clr_bn.grid(row=0, column=3, padx=5)

quit_bn = styled_button(root, "Close", close, "#FF5722")
quit_bn.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", close)
load_task()
root.mainloop()
