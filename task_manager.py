# Command-Line Task Manager with Export
# command_task_manager.py
import os
import json
import csv
import sys
import argparse
from datetime import datetime

# File to store tasks
FILE_NAME = 'tasks.txt'

def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                parts = line.strip().split(' | ')
                if len(parts) >= 3:  # Ensure we have at least ID, title, and status
                    task_id = int(parts[0])
                    title = parts[1]
                    status = parts[2]
                    priority = parts[3] if len(parts) > 3 else "Medium"
                    deadline = parts[4] if len(parts) > 4 else "No deadline"
                    tasks[task_id] = {
                        "title": title, 
                        "status": status, 
                        "priority": priority,
                        "deadline": deadline
                    }
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']} | {task['priority']} | {task['deadline']}\n")

# Export tasks to JSON
def export_to_json(tasks):
    if not tasks:
        print("No tasks to export.")
        return
    
    # Create export data with timestamp
    export_data = {
        "export_date": datetime.now().isoformat(),
        "total_tasks": len(tasks),
        "tasks": []
    }
    
    for task_id, task in tasks.items():
        export_data["tasks"].append({
            "id": task_id,
            "title": task["title"],
            "status": task["status"],
            "priority": task.get("priority", "Medium"),
            "deadline": task.get("deadline", "No deadline")
        })
    
    # Generate filename with timestamp
    filename = f"tasks_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    try:
        with open(filename, 'w') as file:
            json.dump(export_data, file, indent=2)
        print(f"Tasks exported to {filename}")
        print(f"Total tasks exported: {len(tasks)}")
    except Exception as e:
        print(f"Error exporting to JSON: {e}")

# Export tasks to CSV
def export_to_csv(tasks):
    if not tasks:
        print("No tasks to export.")
        return
    
    # Generate filename with timestamp
    filename = f"tasks_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Write header
            writer.writerow(['ID', 'Title', 'Status', 'Priority', 'Deadline'])
            
            # Write task data
            for task_id, task in tasks.items():
                writer.writerow([
                    task_id,
                    task['title'],
                    task['status'],
                    task.get('priority', 'Medium'),
                    task.get('deadline', 'No deadline')
                ])
        
        print(f"Tasks exported to {filename}")
        print(f"Total tasks exported: {len(tasks)}")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")

# Export menu
def export_tasks(tasks):
    if not tasks:
        print("No tasks to export.")
        return
    
    print("\n--- Export Tasks ---")
    print("1. Export to JSON")
    print("2. Export to CSV")
    print("3. Back to main menu")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        export_to_json(tasks)
    elif choice == "2":
        export_to_csv(tasks)
    elif choice == "3":
        return
    else:
        print("Invalid choice. Please try again.")

# Command-line functions for quick operations
def cmd_add_task(args):
    """Add a task via command line"""
    tasks = load_tasks()
    
    priority = args.priority.capitalize() if args.priority else "Medium"
    if priority not in ["High", "Medium", "Low"]:
        print("Error: Priority must be 'high', 'medium', or 'low'")
        return
    
    deadline = args.deadline if args.deadline else "No deadline"
    
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {
        "title": args.title,
        "status": "Pending",
        "priority": priority,
        "deadline": deadline
    }
    
    save_tasks(tasks)
    print(f"✓ Task added successfully!")
    print(f"  ID: {task_id}")
    print(f"  Title: {args.title}")
    print(f"  Priority: {priority}")
    print(f"  Deadline: {deadline}")

def cmd_list_tasks(args):
    """List tasks via command line"""
    tasks = load_tasks()
    
    if args.status:
        # Filter by status
        status_filter = args.status.capitalize()
        if status_filter not in ["Pending", "Completed"]:
            print("Error: Status must be 'pending' or 'completed'")
            return
        tasks = {tid: task for tid, task in tasks.items() if task["status"] == status_filter}
    
    if args.priority:
        # Filter by priority
        priority_filter = args.priority.capitalize()
        if priority_filter not in ["High", "Medium", "Low"]:
            print("Error: Priority must be 'high', 'medium', or 'low'")
            return
        tasks = {tid: task for tid, task in tasks.items() if task.get("priority", "Medium") == priority_filter}
    
    if not tasks:
        print("No tasks found matching the criteria.")
        return
    
    view_tasks(tasks)

def cmd_complete_task(args):
    """Mark a task as completed via command line"""
    tasks = load_tasks()
    
    if args.id not in tasks:
        print(f"Error: Task with ID {args.id} not found.")
        return
    
    tasks[args.id]["status"] = "Completed"
    save_tasks(tasks)
    print(f"✓ Task '{tasks[args.id]['title']}' marked as completed!")

def cmd_delete_task(args):
    """Delete a task via command line"""
    tasks = load_tasks()
    
    if args.id not in tasks:
        print(f"Error: Task with ID {args.id} not found.")
        return
    
    title = tasks[args.id]['title']
    del tasks[args.id]
    save_tasks(tasks)
    print(f"✓ Task '{title}' deleted successfully!")

def cmd_export_tasks(args):
    """Export tasks via command line"""
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks to export.")
        return
    
    if args.format.lower() == "json":
        export_to_json(tasks)
    elif args.format.lower() == "csv":
        export_to_csv(tasks)
    else:
        print("Error: Format must be 'json' or 'csv'")

def setup_cli_parser():
    """Set up command-line argument parser"""
    parser = argparse.ArgumentParser(
        description="Command-Line Task Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python command_task_manager.py add "Buy groceries" -p high -d 2024-01-15
  python command_task_manager.py list
  python command_task_manager.py list -s pending -p high
  python command_task_manager.py complete 1
  python command_task_manager.py delete 2
  python command_task_manager.py export json
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add task command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('-p', '--priority', choices=['high', 'medium', 'low'], 
                           default='medium', help='Task priority (default: medium)')
    add_parser.add_argument('-d', '--deadline', help='Task deadline (YYYY-MM-DD)')
    
    # List tasks command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('-s', '--status', choices=['pending', 'completed'], 
                            help='Filter by status')
    list_parser.add_argument('-p', '--priority', choices=['high', 'medium', 'low'], 
                            help='Filter by priority')
    
    # Complete task command
    complete_parser = subparsers.add_parser('complete', help='Mark task as completed')
    complete_parser.add_argument('id', type=int, help='Task ID to complete')
    
    # Delete task command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID to delete')
    
    # Export tasks command
    export_parser = subparsers.add_parser('export', help='Export tasks')
    export_parser.add_argument('format', choices=['json', 'csv'], help='Export format')
    
    return parser
def add_task(tasks):
    title = input("Enter task title: ")
    
    # Get priority
    print("Select priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")
    priority_choice = input("Enter priority (1-3, default 2): ").strip()
    priority_map = {"1": "High", "2": "Medium", "3": "Low"}
    priority = priority_map.get(priority_choice, "Medium")
    
    # Get deadline
    deadline = input("Enter deadline (YYYY-MM-DD) or press Enter for no deadline: ").strip()
    if not deadline:
        deadline = "No deadline"
    
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {
        "title": title, 
        "status": "Pending", 
        "priority": priority,
        "deadline": deadline
    }
    print(f"Task added with ID: {task_id}")
    print(f"Title: {title}")
    print(f"Priority: {priority}")
    print(f"Deadline: {deadline}")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<4} {'Title':<25} {'Status':<12} {'Priority':<10} {'Deadline':<15}")
    print("="*80)
    
    # Sort tasks by priority (High -> Medium -> Low) then by deadline
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    sorted_tasks = sorted(tasks.items(), key=lambda x: (
        priority_order.get(x[1].get('priority', 'Medium'), 2),
        x[1].get('deadline', 'No deadline') if x[1].get('deadline', 'No deadline') != "No deadline" else "9999-12-31"
    ))
    
    for task_id, task in sorted_tasks:
        title = task['title'][:23] + "..." if len(task['title']) > 25 else task['title']
        status_color = "✓" if task['status'] == "Completed" else "○"
        priority = task.get('priority', 'Medium')
        deadline = task.get('deadline', 'No deadline')
        print(f"{task_id:<4} {title:<25} {status_color} {task['status']:<10} {priority:<10} {deadline:<15}")
    
    print("="*80)

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

# Main function - handles both CLI and interactive modes
def main():
    # Check if command line arguments are provided
    if len(sys.argv) > 1:
        # Command-line mode
        parser = setup_cli_parser()
        args = parser.parse_args()
        
        if args.command == 'add':
            cmd_add_task(args)
        elif args.command == 'list':
            cmd_list_tasks(args)
        elif args.command == 'complete':
            cmd_complete_task(args)
        elif args.command == 'delete':
            cmd_delete_task(args)
        elif args.command == 'export':
            cmd_export_tasks(args)
        else:
            parser.print_help()
    else:
        # Interactive mode
        interactive_mode()

def interactive_mode():
    """Original interactive menu mode"""
    tasks = load_tasks()
    while True:
        print("\n--- Task Manager Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Export Tasks")
        print("6. Exit")
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
            export_tasks(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()