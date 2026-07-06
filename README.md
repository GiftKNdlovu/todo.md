# todo.md

A minimal CLI for managing tasks in a Markdown file. Built for Obsidian vaults, works with any `.md` file using `- [ ]` / `- [x]` syntax.

## What it does

- **List tasks** — shows pending and completed tasks with numbers
- **Add tasks** — appends a new unchecked item
- **Mark done** — toggles a task to completed by number
- **Delete tasks** — removes a task by number
- **Configure file path** — points at any Markdown file (default: `~/obsidian-vault/Todos.md`)

## What it solves

You keep tasks in a Markdown file inside your Obsidian vault (or any folder). This tool lets you manipulate that file from the terminal without opening Obsidian, without a database, and without sync conflicts. The file stays readable and editable by hand.

## Install

```bash
git clone https://github.com/GiftKNdlovu/todo.md.git
cd todo.md
pip install -e .
```

Then `todo` is available everywhere.

Or run directly without installing:

```bash
python -m src.todo list
```

## Usage

```bash
todo setup "/path/to/Todos.md"  # change the target file (once)
todo list                    # show all tasks
todo add "Read case law"     # add a task
todo done 1                  # mark task 1 complete
todo del 2                   # delete task 2
```

## File format

Plain Markdown checkboxes:

```markdown
- [ ] Buy groceries
- [x] Finish essay
```

Only lines matching `- [ ]` or `- [x]` are treated as tasks. Everything else in the file is preserved untouched.

## Requirements

- Python 3.8+
- No external dependencies

## License

MIT