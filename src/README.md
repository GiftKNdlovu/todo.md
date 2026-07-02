# Todo App

A simple terminal-based TODO application that reads and writes tasks to a Markdown file in an Obsidian vault.

## Files

- `todo.py` - Main CLI application (entry point)
- `todo_storage.py` - Handles reading/writing the todo markdown file

## Usage

The application expects a markdown file `Todos.md` in the Obsidian vault at `/home/gift/obsidian-vault/Todos.md`.
Each task is a list item:
- [ ] task description
- [x] completed task

### Commands

- `todo list`  
  Show all pending and completed tasks.

- `todo add "task description"`  
  Append a new pending task.

- `todo done <index>`  
  Mark a pending task as completed (index shown by `todo list`).

- `todo del <index>`  
  Delete a task by its index (shown by `todo list`).

### Example

```bash
$ todo list
1. [ ] Buy groceries
2. [x] Walk the dog

$ todo add "Read book"
Added: "Read book"

$ todo list
1. [ ] Buy groceries
2. [x] Walk the dog
3. [ ] Read book

$ todo done 1
Marked task 1 as completed.

$ todo del 3
Deleted: "Read book"

$ todo list
1. [x] Buy groceries
2. [x] Walk the dog
```

### Dependencies

- Python 3.8+ (standard library only, no external packages required)

### Notes

- The application reads and writes the entire markdown file each time, preserving any existing formatting outside of task lines.
- Task indices are based on the order shown by `todo list` (starting at 1).