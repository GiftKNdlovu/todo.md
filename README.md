# todo.md

Simple TODO CLI app that integrates with an Obsidian vault markdown file.

The todo file is located at: `/home/gift/obsidian-vault/Todos.md` by default.
You can change the location using the `setup` command.

Usage:
    todo list          - Show all tasks
    todo add "task"    - Add a new task
    todo done <num>    - Mark task as done (1-indexed)
    todo del <num>     - Delete task (1-indexed)
    todo setup <path>  - Set the todo file path (first time setup)

Example:
    todo add "Buy groceries"
    todo list
    todo done 1

The todo file uses markdown format compatible with Obsidian:
- [ ] task text   (incomplete)
- [x] task text   (complete)