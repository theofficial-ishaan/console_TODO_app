# console_TODO_app
A simple command-line To-Do List application written in Python. This app allows you to add, remove, and complete tasks, with all tasks saved to a local JSON file for persistence.

## Features
- Add new tasks with optional due dates
- Remove tasks by index
- Mark tasks as completed
- Persistent storage using a JSON file (`tasks.json`)
- Simple command-line interface

## Requirements
- Python 3.x

## Installation
1. Clone or download this repository to your local machine.
2. Ensure you have Python 3 installed.

## Usage
1. Open a terminal and navigate to the project directory.
2. Run the application:
   ```
   python todo_app.py
   ```
3. Follow the on-screen prompts to add, remove, or complete tasks.

### Commands
- `add` or `1`: Add a new task
- `remove` or `2`: Remove a task by its index
- `complete` or `3`: Mark a task as completed
- `exit` or `4`: Save and exit the application

## Data Storage
- All tasks are stored in `tasks.json` in the project directory.

## Example
```
Your To-Do List:
1. [✗] Present To-Do app: Today

Commands: 1.add, 2.remove, 3.complete, 4.exit
Enter command: add
Task title: Buy groceries
Due (optional): Tomorrow
[Task added successfully.]
```

## License
This project is licensed under the MIT License.

## Contact
For questions or suggestions, please open an issue or contact the author.
