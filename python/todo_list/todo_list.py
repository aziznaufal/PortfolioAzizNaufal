import customtkinter as ctk
from tkinter import messagebox
import json
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Main app
app = ctk.CTk()
app.title("Modern To-Do List")
app.geometry("400x500")
app.resizable(False, False)

# JSON file path
TASKS_FILE = "tasks.json"

# Function to load tasks from JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save tasks to JSON file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Task list will be stored here
tasks = load_tasks()

# --- Functions ---
def refresh_tasks():
    # Clear current list
    for widget in task_frame.winfo_children():
        widget.destroy()

    # Rebuild task display
    for index, task in enumerate(tasks):
        task_row = ctk.CTkFrame(task_frame)
        task_row.pack(fill="x", pady=2, padx=5)

        task_label = ctk.CTkLabel(task_row, text=task, anchor="w")
        task_label.pack(side="left", fill="x", expand=True, padx=(10, 0))

        delete_btn = ctk.CTkButton(task_row, text="❌", width=30, fg_color="red",
                                   command=lambda i=index: delete_task(i))
        delete_btn.pack(side="right", padx=5)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        entry.delete(0, "end")
        save_tasks()  # Save tasks to JSON file after adding
        refresh_tasks()
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def delete_task(index):
    tasks.pop(index)
    save_tasks()  # Save tasks to JSON file after deleting
    refresh_tasks()

def clear_all():
    if messagebox.askyesno("Clear All", "Delete all tasks?"):
        tasks.clear()
        save_tasks()  # Save tasks to JSON file after clearing
        refresh_tasks()

# --- UI Elements ---
title = ctk.CTkLabel(app, text="📝 To-Do List", font=ctk.CTkFont(size=20, weight="bold"))
title.pack(pady=15)

entry = ctk.CTkEntry(app, placeholder_text="Enter a task...", width=280)
entry.pack(pady=5)

add_btn = ctk.CTkButton(app, text="Add Task", command=add_task)
add_btn.pack(pady=5)

clear_btn = ctk.CTkButton(app, text="Clear All", fg_color="red", command=clear_all)
clear_btn.pack(pady=5)

# Scrollable task list
task_frame = ctk.CTkScrollableFrame(app, width=360, height=300)
task_frame.pack(pady=10, fill="both", expand=True)

# Initial refresh to display tasks loaded from JSON
refresh_tasks()

# Main loop
app.mainloop()
