import argparse
from functions import load_database, save_database, add_task, list_task, update_task, delete_task

def main():
    parser = argparse.ArgumentParser('Taskly - task manager')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('description')

    



