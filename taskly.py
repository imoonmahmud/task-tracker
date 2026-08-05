import argparse
import json
from datetime import datetime


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

def add_task(database, description):
    existing_ids = [task['id'] for task in database]
    next_id = max(existing_ids) + 1 if existing_ids else 1
    today = datetime.now().strftime('%Y-%m-%d')

    task = {
        'id': next_id,
        'description': description,
        'status': 'todo',
        'created_at': today
    }
    database.append(task)
    return task

file_path = 'tasks.json'
database = load_database(file_path)
new_task = add_task(database, 'Go to teach Hamim')
save_database(database, file_path)
print(f'Task added successfully (id: {new_task['id']})')

