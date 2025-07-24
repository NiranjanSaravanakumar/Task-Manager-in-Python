import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task.description} (Due: {task.due_date})")

    def set_reminder(self, task_idx, reminder_date):
        try:
            task = self.tasks[task_idx - 1]
            if task.due_date < reminder_date:
                print("Reminder set successfully!")
            else:
                print("Reminder date should be after the task's due date.")
        except IndexError:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    # Example tasks
    task_manager.add_task(Task("Finish report", datetime.date(2024, 3, 20)))
    task_manager.add_task(Task("Submit assignment", datetime.date(2024, 3, 25)))

    while True:
        print("\nTask Management Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Set Reminder")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = datetime.date.fromisoformat(input("Enter due date (YYYY-MM-DD): "))
            task_manager.add_task(Task(description, due_date))
            print("Task added successfully!")
        elif choice == '2':
            task_manager.display_tasks()
        elif choice == '3':
            task_manager.display_tasks()
            task_idx = int(input("Enter the index of the task to set reminder for: "))
            reminder_date = datetime.date.fromisoformat(input("Enter reminder date (YYYY-MM-DD): "))
            task_manager.set_reminder(task_idx, reminder_date)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
