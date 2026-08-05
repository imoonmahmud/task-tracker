import argparse

parser = argparse.ArgumentParser(description='Taskly - a task manager')
subparsers = parser.add_subparsers(dest='command')
add_parser = subparsers.add_parser('add', help='Add a new task')
add_parser.add_argument('description', help='The task description')

args = parser.parse_args()
print(args.command)
print(args.description)

