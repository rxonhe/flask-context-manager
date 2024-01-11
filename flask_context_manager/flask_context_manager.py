import argparse
import os


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)


def setup_project_structure():
    base_dirs = [
        'src/main/config',
        'src/main/service',
        'src/main/controller',
        'src/main/resources',
        'src/test/resources'
    ]

    for dir in base_dirs:
        create_directory(dir)

    create_file('src/main/resources/config.ini')
    create_file('src/test/resources/config.ini')

    print("Flask Context Manager structure successfully created!")


def main():
    parser = argparse.ArgumentParser(description='Flask Context Manager CLI')
    parser.add_argument('command', choices=['start'], help='Command to execute')

    args = parser.parse_args()

    if args.command == 'start':
        setup_project_structure()


if __name__ == "__main__":
    main()
