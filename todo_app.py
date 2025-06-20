import json
import os


class Task:
    """Class representing a single task in the To-Do application."""

    def __init__(self, title, due="", Status="not started", completed=False):
        self.title = title
        self.due = due
        self.Status = Status 
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "due": self.due,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data.get("title", "Empty Task"),
            due=data.get("due", "Today"),
            completed=data.get("completed", False)
        )

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}: {self.due}"


class TaskAttributes(Task):
    """A Derived class for Task with additional attributes that we plan to add in future."""
    pass


class ToDoApp:
    """Main class for the To-Do application, managing tasks and user interactions."""

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, due=""):
        task = Task(title, due)
        self.tasks.append(task)
        print("[Task added successfully.]")

    def remove_task(self,idx):
        if 1 <= idx <= len(self.tasks):
            removed = self.tasks.pop(idx - 1)
            print(f"Removed task: {removed.title}")
        else:   
            print("[Invalid task number.]")

    def list_tasks(self):
        if not self.tasks:
            print("[No tasks found.]")
            return
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def complete_task(self, idx):
        if 1 <= idx <= len(self.tasks):
            self.tasks[idx - 1].mark_completed()
            print("[Task marked as completed.]")
        else:
            print("[Invalid task number.]")

    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)


    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        else:
            self.tasks = []


    def run(self):
        """Main loop for the To-Do application which keeps the application running until user exits."""

        while True:
            print("\nYour To-Do List:")
            self.list_tasks()
            print("\nCommands: 1.add, 2.remove, 3.complete, 4.exit")
            cmd = input("Enter command: ").strip().lower()
            
            if cmd == "add" or cmd == "1":

                title = input("Task title: ").strip()
                if not title:
                    print("[Task title cannot be empty.]")
                    continue
                due = input("Due (optional): ").strip()
                if not due:
                    due = "Today"
                self.add_task(title, due)
                self.save_tasks()

            elif cmd == "remove" or cmd == "2":
                try:
                    if not self.tasks:
                        print("[No tasks stored to remove.]")
                        continue
                    idx = int(input("Task index to remove: ").strip())
                    self.remove_task(idx)
                    self.save_tasks()
                except ValueError:
                    print("[Please enter a valid index.]")                   
                
            
            elif cmd == "complete" or cmd == "3":
                try:
                    if not self.tasks:
                        print("[No tasks stored to mark complete.]")
                        continue
                    idx = int(input("Task index to complete: "))
                    self.complete_task(idx)
                    self.save_tasks()
                except ValueError:
                    print("[Please enter a valid index.]")
            
            elif cmd == "exit" or cmd == "4":
                self.save_tasks()
                print("[Autosaving....]")
                print("[Goodbye!]")
                break
            
            else:
                print("[Unknown command. Please try again.]")


if __name__ == "__main__":
    app = ToDoApp()
    app.run()