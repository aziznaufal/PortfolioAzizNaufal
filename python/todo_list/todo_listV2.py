import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import json, os

import os
import sys
from pathlib import Path

def resource_path(filename):
    # When running from a PyInstaller bundle
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return filename

def get_data_path():
    # Create app-specific folder inside user's home directory
    app_data_dir = Path.home() / ".todo_list"
    app_data_dir.mkdir(exist_ok=True)
    return app_data_dir / "tasks.json"

TASKS_FILE = get_data_path()

print(f'TASKS_FILE - {TASKS_FILE}')

def extract_date(item):
    return datetime.fromisoformat(item['done_date'])

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                data = json.load(file)
                # Validate structure
                if isinstance(data, dict):
                    data.setdefault("active", [])
                    data.setdefault("done", [])
                    data["active"] = [t for t in data["active"] if isinstance(t, dict) and "title" in t]
                    data["done"] = [t for t in data["done"] if isinstance(t, dict) and "title" in t]
                    return data
        except (json.JSONDecodeError, ValueError):
            print("Invalid tasks file. Resetting.")
    return {"active": [], "done": []}


def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = task_entry.get().strip()
    due = due_date.get_date()
    if not title:
        messagebox.showwarning("Empty Task", "Task title cannot be empty.")
        return
    task = {
        "title": title,
        "due_date": due.strftime("%Y-%m-%d"),
        "done_date": "",
        "notes": "",
        "history": []
    }
    tasks["active"].append(task)
    save_tasks()
    task_entry.delete(0, tk.END)
    refresh_tasks()

def mark_done(index):
    task = tasks["active"].pop(index)
    task["history"].append(f"Marked done at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    task["done_date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tasks["done"].append(task)
    save_tasks()
    refresh_tasks()
    show_detail(-1)  # Hide detail view

def update_notes(index, new_notes):
    tasks["active"][index]["notes"] = new_notes
    tasks["active"][index]["history"].append(f"Notes updated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {new_notes}")
    save_tasks()
    refresh_tasks()
    show_detail(index)

def refresh_tasks():
    for widget in active_list.winfo_children():
        widget.destroy()
    for widget in done_list.winfo_children():
        widget.destroy()

    # Filter out invalid tasks
    tasks["active"] = [t for t in tasks["active"] if isinstance(t, dict) and "title" in t and "due_date" in t]
    tasks["done"] = [t for t in tasks["done"] if isinstance(t, dict) and "title" in t and "due_date" in t]

    for idx, task in enumerate(tasks["active"]):
        title = task.get("title", "Untitled")
        due = task.get("due_date", "N/A")
        btn = ctk.CTkButton(active_list, text=f"{title} (Due: {due})", anchor="w",
                            command=lambda i=idx: show_detail(i))
        btn.pack(fill="x", pady=2, padx=5)

    sorted_data = sorted(tasks["done"], key=extract_date, reverse=True)
    for task in sorted_data:
        frame = ctk.CTkFrame(done_list)
        frame.pack(fill="x", pady=2, padx=5)
        ctk.CTkLabel(frame, text=f"{task.get('title', 'Untitled')} (Done)", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=10)
        ctk.CTkLabel(frame, text=f"Due: {task.get('due_date', 'N/A')} | Notes: {task.get('notes', '')}").pack(anchor="w", padx=10)
        for h in task.get("history", []):
            ctk.CTkLabel(frame, text=f" - {h}", text_color="gray").pack(anchor="w", padx=20)


def show_detail(index):
    for widget in detail_frame.winfo_children():
        widget.destroy()

    if index == -1 or index >= len(tasks["active"]):
        return

    task = tasks["active"][index]
    notes = ''
    for data in task['history']:
        notes += (f"{data} \n")
        print('notes - ', notes)

    ctk.CTkLabel(detail_frame, text=f"Task: {task['title']}", font=ctk.CTkFont(size=15, weight="bold")).pack(anchor="w", padx=10, pady=(5, 0))
    ctk.CTkLabel(detail_frame, text=f"Due: {task['due_date']}").pack(anchor="w", padx=10)

    ctk.CTkLabel(detail_frame, text="Notes:").pack(anchor="w", padx=10, pady=(10, 0))
    ctk.CTkLabel(detail_frame, text=notes).pack(anchor="w", padx=10, pady=(10, 0))
    notes_entry = ctk.CTkEntry(detail_frame)
    notes_entry.insert(0, task.get("notes", ""))
    notes_entry.pack(padx=10, pady=5, fill="x")

    ctk.CTkButton(detail_frame, text="Save Notes", command=lambda: update_notes(index, notes_entry.get())).pack(padx=10, pady=5)
    ctk.CTkButton(detail_frame, text="Mark as Done", fg_color="green", command=lambda: mark_done(index)).pack(padx=10, pady=5)

# Setup UI
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Modern Todo List App")
app.geometry("700x600")

tasks = load_tasks()

# Input frame
input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=10, fill="x")

task_entry = ctk.CTkEntry(input_frame, placeholder_text="Enter Task Title")
task_entry.pack(padx=10, pady=5, fill="x")

due_date = DateEntry(input_frame, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
due_date.pack(padx=10, pady=5)

ctk.CTkButton(input_frame, text="Add Task", command=add_task).pack(padx=10, pady=10)

# Task split frames
split_frame = ctk.CTkFrame(app)
split_frame.pack(fill="both", expand=True, padx=10)

left_frame = ctk.CTkFrame(split_frame)
left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

right_frame = ctk.CTkFrame(split_frame)
right_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

ctk.CTkLabel(left_frame, text="Active Tasks", font=ctk.CTkFont(size=16, weight="bold")).pack()
active_list = ctk.CTkScrollableFrame(left_frame)
active_list.pack(fill="both", expand=True, padx=5, pady=5)

ctk.CTkLabel(right_frame, text="Task Details", font=ctk.CTkFont(size=16, weight="bold")).pack()
detail_frame = ctk.CTkFrame(right_frame)
detail_frame.pack(fill="both", expand=True, padx=5, pady=5)

# Done section
ctk.CTkLabel(app, text="Completed Tasks", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 0))
done_list = ctk.CTkScrollableFrame(app, height=150)
done_list.pack(fill="both", expand=False, padx=10, pady=(0, 10))

refresh_tasks()
app.mainloop()
