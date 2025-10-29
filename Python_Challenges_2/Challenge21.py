#this program allowss users to create a to-do list where they can add, view and remove tasks.

from datetime import date, datetime

def show_menu():
    print("Hello! Here is the To-Do List Menu:")
    print("1. View all task in the to-do list")
    print("2. Add task to the to-do list")
    print("3. Remove task from the to-do list")
    print("4. Search for a task by prioirty")
    print("5. Exit")

def view_all_tasks(tasks):
    if not tasks:
        print("You have no tasks in your to-do list")
    else:
        for task, details in tasks.items():
            print(f"Task: {task}, Description: {details['description']}, Priority: {details['priority']}, Due date: {details['due_date']}")

def add_task(tasks):
    task_name = input("Enter task name to add in the to-do list: ").strip()
    if task_name in tasks:
        print("This task already exists in the to-do list!")
        return

    description = input("Enter task description: ").strip()

    
    while True:
        priority = input("Enter priority (high, medium, low): ").strip().lower()
        if priority in ["high", "medium", "low"]:
            break
        else:
            print("Invalid priority! Please enter 'high', 'medium', or 'low'.")

    
    while True:
        try:
            print("Enter the due date for this task:")
            day = int(input("Enter the day (1-31): "))
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year (e.g., 2025): "))

            due_date = date(year, month, day)
            today = date.today()

            if due_date < today:
                print("You cannot set a due date in the past. Please enter a date from today onwards.")
            else:
                break
        except ValueError:
            print("Invalid date! Please enter a valid day, month, and year.")

    tasks[task_name] = {
        "description": description,
        "priority": priority,
        "due_date": due_date.strftime("%d-%m-%Y")  
    }

    print(f"Task '{task_name}' added successfully!")


def remove_task(tasks):

    task_name = input("Enter the task name for the task to be deleted: ").strip()

    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' has been deleted from the to-do list")

    else:
        print("Task has not been found in the to-do list")


def search_task_by_priority(tasks):
    priority = input("Enter the piroity for task search (high, medium, low): ").strip().lower()

    filtered_tasks = {t: d for t, d in tasks.items() if d["priority"] == priority}


    if filtered_tasks:
        print(f"Tasks with priority '{priority}': ")

        for task, details in filtered_tasks.items():
            print(f"{task}: {details['description']} (Due date: {details['due_date']})")
    
    else:
        print(f"There are no tasks with the priority '{priority}'")


def program():
    tasks = {}

    while True:

        show_menu()

        option = input("Choose an option between 1 and 5: ").strip()


        if option == "1":
            view_all_tasks(tasks)
        elif option == "2":
            add_task(tasks)
        elif option == "3":
            remove_task(tasks)
        elif option == "4":
            search_task_by_priority(tasks)
        elif option == "5":
            print("You have exited the to-do list program!")
            break

        else:
            print("Invalid option. Please select a valid option between 1 and 5")


program()

