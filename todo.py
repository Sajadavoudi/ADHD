import datetime
import tkinter as tk

# Define an empty list to store tasks
tasks = []

# Define a function to add a task to the list
def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    due_date = datetime.datetime.strptime(date_entry.get(), "%Y-%m-%d").date()
    reminders = reminders_entry.get().split(",")
    tasks.append({
        "description": task,
        "priority": priority,
        "due_date": due_date,
        "completed": False,
        "reminders": reminders,
    })
    task_entry.delete(0, tk.END)
    priority_var.set("low")
    date_entry.delete(0, tk.END)
    reminders_entry.delete(0, tk.END)

# Define a function to mark a task as completed
def complete_task():
    task = task_listbox.get(tk.ACTIVE)
    for t in tasks:
        if t["description"] == task:
            t["completed"] = True
            task_listbox.itemconfig(tk.ACTIVE, fg="gray")
            break

# Define a function to display the list of tasks
def show_tasks():
    task_listbox.delete(0, tk.END)
    for task in sorted(tasks, key=lambda t: (t["priority"], t["due_date"])):
        if not task["completed"]:
            task_listbox.insert(tk.END, "- {} ({}) - Due: {}".format(task["description"], task["priority"], task["due_date"].strftime("%Y-%m-%d")))
            if task["reminders"]:
                task_listbox.insert(tk.END, "    Reminders: {}".format(", ".join(task["reminders"])))

# Create the GUI window
window = tk.Tk()
window.title("To-Do List")

# Create the GUI widgets
task_label = tk.Label(window, text="Task:")
task_entry = tk.Entry(window)
priority_label = tk.Label(window, text="Priority:")
priority_var = tk.StringVar(value="low")
priority_low = tk.Radiobutton(window, text="Low", variable=priority_var, value="low")
priority_medium = tk.Radiobutton(window, text="Medium", variable=priority_var, value="medium")
priority_high = tk.Radiobutton(window, text="High", variable=priority_var, value="high")
date_label = tk.Label(window, text="Due Date (YYYY-MM-DD):")
date_entry = tk.Entry(window)
reminders_label = tk.Label(window, text="Reminders (separated by commas):")
reminders_entry = tk.Entry(window)
add_button = tk.Button(window, text="Add Task", command=add_task)
complete_button = tk.Button(window, text="Mark Completed", command=complete_task)
task_listbox = tk.Listbox(window, width=50)

# Add the widgets to the window
task_label.grid(row=0, column=0, sticky="W")
task_entry.grid(row=0, column=1)
priority_label.grid(row=1, column=0, sticky="W")
priority_low.grid(row=1, column=1, sticky="W")
priority_medium.grid(row=1, column=1, sticky="E")
priority_high.grid(row=1, column=1, sticky="E")
date_label.grid(row=2, column=0, sticky="W")
date_entry.grid(row=2, column=1)
reminders_label.grid(row=3, column=0, sticky="E")
reminders_entry.grid(row=3, column=1)
add_button.grid(row=4, column=0, pady=10)
complete_button.grid(row=4, column=1, pady=10)
task_listbox.grid(row=5, column=0, columnspan=2)

#Display the GUI window
show_tasks()
window.mainloop()
