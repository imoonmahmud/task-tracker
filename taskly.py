import argparse
import json

parser = argparse.ArgumentParser(description='Taskly - a task manager')
subparsers = parser.add_subparsers(dest='command')
add_parser = subparsers.add_parser('add', help='Add a new task')
add_parser.add_argument('description', help='The task description')

args = parser.parse_args()

def load_database(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_database(database, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(database, file, indent=4)

tasks = load_database('tasks.json')
print(tasks)

tasks.append({"id": 1, "description": "test task", "status": "todo", "created_at": "2026-08-05"})
save_database(tasks, "tasks.json")

