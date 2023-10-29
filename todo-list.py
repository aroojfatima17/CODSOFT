# Initializing to-do list
todo_list = {}


def add_task():
    task_name = input("Enter the task name: ")
    task_description = input("Enter a description for the task: ")
    task_status = input("Enter the task status (completed/pending/urgent/in progress): ").lower()

    if task_status not in ("completed", "pending", "urgent", "in progress"):
        print("Invalid status. Please choose from 'completed', 'pending', 'urgent', or 'in progress'.")
        return

    todo_list[task_name] = {"description": task_description, "status": task_status}
    print(f"Task '{task_name}' added to the to-do list with status '{task_status}'.")


def update_task_status():
    task_name = input("Enter the task name you want to update: ")
    if task_name in todo_list:
        new_status = input("Enter the new status (completed/pending/urgent/in progress): ").lower()
        if new_status in ("completed", "pending", "urgent", "in progress"):
            todo_list[task_name]["status"] = new_status
            print(f"Task '{task_name}' status updated to '{new_status}'.")
        else:
            print("Invalid status. Please choose from 'completed', 'pending', 'urgent', or 'in progress'.")
    else:
        print(f"Task '{task_name}' not found in the to-do list.")


def view_tasks(status_filter=None):
    print("To-Do List:")
    for task_name, task_info in todo_list.items():
        if status_filter is None or task_info["status"] == status_filter:
            print(f"{task_name} - {task_info['description']} - {task_info['status']}")


while True:
    print("Options:")
    print("1: Add a task")
    print("2: Update task status")
    print("3: View all tasks")
    print("4: View completed tasks")
    print("5: View pending tasks")
    print("6: View urgent tasks")
    print("7: View in progress tasks")
    print("8: Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        update_task_status()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        view_tasks("completed")
    elif choice == "5":
        view_tasks("pending")
    elif choice == "6":
        view_tasks("urgent")
    elif choice == "7":
        view_tasks("in progress")
    elif choice == "8":
        break
    else:
        print("Invalid input. Please enter a valid option (1-8).")

print("To-Do List Application has ended.")
