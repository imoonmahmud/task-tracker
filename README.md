# CLI TODO App

Taskly is a simple command-line task manager built in Python. Add, list, update, and track tasks, all stored locally in a JSON file.

Built as a learning project to practice file I/O, JSON handling, and building command-line interfaces with `argparse`.

## Features

- Add new tasks
- List tasks, with optional filtering by status
- Update a task's description and/or status
- Mark tasks as `todo`, `in-progress`, or `done`
- Delete tasks
- Tasks persist between runs in a local `tasks.json` file

## Installation

```bash
git clone https://github.com/imoonmahmud/task-tracker.git
```

## Usage

### Add a task
```bash
python taskly.py add "Buy groceries"
```
```
Task added successfully (ID: 1)
```

### List tasks
```bash
python taskly.py list
python taskly.py list -s done          # only done tasks
python taskly.py list -s in-progress   # only in-progress tasks
```
```
[1] todo         Buy groceries             (2026-08-07)
[2] in-progress  Walk the dog              (2026-08-07)
```

### Update a task
```bash
python taskly.py update 1 "Buy groceries and milk"     # change description
python taskly.py update 1 -s done                      # change status
python taskly.py update 1 "New text" -s in-progress     # change both
```

### Delete a task
```bash
python taskly.py delete 1
```

## How it works

Tasks are stored as a list of dictionaries in `tasks.json`:

```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "created_at": "2026-08-07"
    }
]
```

Each command loads the full task list from `tasks.json`, makes its change in memory, then saves the whole list back to disk. Task IDs are assigned automatically by taking the highest existing ID and adding one.

https://roadmap.sh/projects/task-tracker
