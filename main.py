class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task: {self.title}, Description: {self.description}, Status: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Added task: {task.title}")

    def remove_task(self, title):
        task_to_remove = None
        for task in self.tasks:
            if task.title == title:
                task_to_remove = task
                break
        if task_to_remove:
            self.tasks.remove(task_to_remove)
            print(f"Removed task: {title}")
        else:
            print(f"Task not found: {title}")

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Task marked as completed: {title}")
                return
        print(f"Task not found: {title}")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)


def display_menu():
    print("\n1. Add a Task")
    print("2. Remove a Task")
    print("3. Mark Task as Completed")
    print("4. Show All Tasks")
    print("5. Exit")


if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            todo_list.add_task(title, description)

        elif choice == "2":
            title = input("Enter the title of the task to remove: ")
            todo_list.remove_task(title)

        elif choice == "3":
            title = input("Enter the title of the task to mark as completed: ")
            todo_list.mark_task_completed(title)

        elif choice == "4":
            print("\nTo-Do List:")
            todo_list.show_tasks()

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 5.")
