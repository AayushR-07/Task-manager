import json
import os

# Define the file to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from the file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour tasks:")
    for index, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status}")

# Add a new task
def add_task(tasks):
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task_name}' added!")

# Mark a task as complete
def mark_task_complete(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        if tasks[task_index]["completed"]:
            print("This task is already completed.")
        else:
            tasks[task_index]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[task_index]['task']}' marked as complete!")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        task_name = tasks[task_index]["task"]
        tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{task_name}' deleted!")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

# Main menu
def main():
    print("Welcome to the Personal Task Manager!")
    tasks = load_tasks()

    while True:
        print("\n1. View tasks")
        print("2. Add task")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
