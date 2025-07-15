# Command-Line Task Manager
# command_task_manager.py
import os

# File to store tasks
FILE_NAME = 'tasks.txt'

def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                task_id, title, status = line.strip().split(' | ')
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "Pending"}
    print(f"Task added with ID: {task_id}")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for task_id, task in tasks.items():
        print(f"ID: {task_id}, Title: {task['title']}, Status: {task['status']}")

# Mark a task as completed
def mark_task_completed(tasks):
    task_id = int(input("Enter task ID to mark as completed: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "Completed"
        print(f"Task '{tasks[task_id]['title']}' marked as completed.")
    else:
        print("Task ID not found.")

# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        title = tasks[task_id]['title']  # Get title before deleting
        del tasks[task_id]
        print(f"Task '{title}' deleted.")
    else:
        print("Task ID not found.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n--- Task Manager Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()