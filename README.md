# Command-Line Task Manager

This script ([command_task_manager.py](command_task_manager.py)) provides a simple command-line interface for managing tasks. Tasks are stored in a text file ([tasks.txt](tasks.txt)) and can be added, viewed, marked as completed, or deleted.

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Persistent storage in `tasks.txt`

## Usage

Run the script in your terminal:

```sh
python [command_task_manager.py]
Here’s an updated README for practice2.py:

Follow the menu prompts to manage your tasks.

Command-Line Mode
You can use subcommands for automation:

Add a task:
python practice2.py add "Buy groceries" -p high -d 2025-07-20 

List tasks:
python practice2.py list
python practice2.py list -s pending -p high

Mark as completed:
python practice2.py complete 1

Delete a task:
python practice2.py delete 2

Export tasks:
python practice2.py export json
python practice2.py export csv

Data Storage
Tasks are saved in tasks.txt in this format:
task_id | title | status | priority | deadline

Example:
1 | Buy groceries | Pending | High | 2025-07-20

Requirements
Python 3.x
No external dependencies required.
