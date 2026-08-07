import argparse
from functions import load_database, save_database, add_task, list_task, update_task, delete_task


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    add_parser = subparser.add_parser('add')
    add_parser.add_argument('description')

    list_parser = subparser.add_parser('list')
    list_parser.add_argument('-s', '--status', choices=['todo', 'in-progress', 'done', 'all'], default='all')

    update_parser = subparser.add_parser('update')
    update_parser.add_argument('task_id', type=int)
    update_parser.add_argument('description', nargs='?', default=None)
    update_parser.add_argument('-s', '--status', choices=['todo','in-progress', 'done'])

    delete_parser = subparser.add_parser('delete')
    delete_parser.add_argument('task_id', type=int)


    args = parser.parse_args()
    file_path = 'tasks.json'
    database = load_database(file_path)

    if args.command == 'add':
        task = add_task(database, args.description)
        save_database(database, file_path)
        print(f'Task added successfully (ID: {task['id']})')
    elif args.command == 'list':
        list_task(database, args.status)
    elif args.command == 'update':
        task = update_task(database, args.task_id, new_description=args.description, new_status=args.status)
        if task is None:
            print(f'No task found with ID {args.task_id}')
        else:
            save_database(database, file_path)
            print(f'Task {args.task_id} updated successfully')
    elif args.command == 'delete':
        if delete_task(database, args.task_id):
            save_database(database, file_path)
            print(f'Task deleted successfully (ID: {args.task_id})')
        else:
            print(f'No task found with ID {args.task_id}')
            

if __name__ == '__main__':
    main()


 
