import json
from datetime import datetime

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

def list_task(database, status=None):
    if status is None or status == 'all':
        filtered = database
    else:
        filtered = [task for task in database if task['status'] == status]

    if not filtered:
        print('No tasks found.')
        return
    for task in filtered:
        print(f"[{task['id']}] {task['status']:<12} {task['description']:<25} ({task['created_at']})")

def update_task(database, task_id, new_description=None, new_status=None):
    for task in database:
        if task['id'] == task_id:
            if new_description is not None:
                task['description'] = new_description
            if new_status is not None:
                task['status'] = new_status
            return task
    return None

def delete_task(database, task_id):
    new_database = [task for task in database if task['id'] != task_id]
    if len(new_database) == len(database):
        return False
    database[:] = new_database
    return True