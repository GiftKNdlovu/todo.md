import os

TODO_FILE = "/home/gift/obsidian-vault/Todos.md"

def read_todos():
    """Return list of (completed, text) tuples."""
    if not os.path.exists(TODO_FILE):
        return []
    todos = []
    with open(TODO_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith('- [ ]'):
                todos.append((False, stripped[5:].strip()))
            elif stripped.startswith('- [x]'):
                todos.append((True, stripped[5:].strip()))
    return todos

def write_todos(todos):
    """Overwrite the todo file with the given list of (completed, text)."""
    lines = []
    for completed, text in todos:
        marker = '[x]' if completed else '[ ]'
        lines.append(f'- {marker} {text}')
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
        if lines:
            f.write('\n')

def add_todo(text):
    todos = read_todos()
    todos.append((False, text))
    write_todos(todos)

def mark_done(index):
    """Mark the todo at 0-based index as done. Return True if successful."""
    todos = read_todos()
    if 0 <= len(todos) and index < len(todos):
        if not todos[index][0]:
            todos[index] = (True, todos[index][1])
            write_todos(todos)
            return True
        else:
            return False  # already done
    return False

def delete_todo(index):
    """Delete the todo at 0-based index. Return True if successful."""
    todos = read_todos()
    if 0 <= index < len(todos):
        del todos[index]
        write_todos(todos)
        return True
    return False

def list_todos():
    return read_todos()