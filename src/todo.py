#!/usr/bin/env python3
"""
Simple TODO CLI app that integrates with an Obsidian vault markdown file.
Usage:
    todo list          - Show all tasks
    todo add "task"    - Add a new task
    todo done <num>    - Mark task as done (1-indexed)
    todo del <num>     - Delete task (1-indexed)
    todo setup <path>  - Set up the todo file location (first time setup)
"""

import sys
from todo_storage import (
    add_todo,
    delete_todo,
    list_todos,
    mark_done,
    set_todo_file,
    get_todo_file,
)

def print_usage():
    print(__doc__.strip())

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]

    if command == "list":
        todos = list_todos()
        if not todos:
            print("No tasks.")
            return
        for i, (done, text) in enumerate(todos, start=1):
            status = "x" if done else " "
            print(f"{i}. [{status}] {text}")

    elif command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing task description.")
            print('Usage: todo add "task description"')
            return
        task = " ".join(sys.argv[2:])
        add_todo(task)
        print(f'Added: "{task}"')

    elif command == "done":
        if len(sys.argv) < 3:
            print("Error: Missing task number.")
            print('Usage: todo done <task-number>')
            return
        try:
            idx = int(sys.argv[2]) - 1  # convert to 0-based
        except ValueError:
            print("Error: Task number must be an integer.")
            return
        if mark_done(idx):
            print(f"Marked task {idx + 1} as done.")
        else:
            print(f"Error: Could not mark task {idx + 1} as done (maybe already done or out of range).")

    elif command == "del" or command == "delete":
        if len(sys.argv) < 3:
            print("Error: Missing task number.")
            print('Usage: todo del <task-number>')
            return
        try:
            idx = int(sys.argv[2]) - 1
        except ValueError:
            print("Error: Task number must be an integer.")
            return
        if delete_todo(idx):
            print(f"Deleted task {idx + 1}.")
        else:
            print(f"Error: Could not delete task {idx + 1} (out of range).")

    elif command == "setup":
        if len(sys.argv) < 3:
            current_file = get_todo_file()
            print(f"Current todo file: {current_file}")
            print('Usage: todo setup "/path/to/your/Todos.md"')
            print("Example: todo setup \"/home/gift/obsidian-vault/Todos.md\"")
            return
        path = " ".join(sys.argv[2:])
        set_todo_file(path)
        print(f"Todo file location set to: {path}")

    else:
        print(f"Error: Unknown command '{command}'.")
        print_usage()

if __name__ == "__main__":
    main()