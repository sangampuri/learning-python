def load_tasks():
    try:
        with open('todore.txt', 'r') as file:
            tasks_list = file.read()
            tasks_list = tasks_list.splitlines()
            for task in tasks_list:
                tasks.append(task)
    except FileNotFoundError:
        print("No existing task file found. Starting with an empty task list.")

tasks = []
load_tasks()

def add_task():
    while True:
        new_task = input('Enter a new task: ')
        new_task = new_task.strip().lower() 
        if new_task != 'done':
            tasks.append(new_task)
        elif new_task == 'done':
            break

def show_tasks():
    print('Your tasks:')
    for key, task in enumerate(tasks,1):
        print(f'{key}. {task}')

def remove_task():
    show_tasks()
    task_to_remove = int(input('Enter the number of the task to remove: '))
    task_to_remove -= 1 
    if 0 <= task_to_remove < len(tasks):
        removed_task = tasks.pop(task_to_remove)
        print(f'Task "{removed_task}" removed.')

def main_menu():
    print('\nTo-Do List Menu:')
    print('1. Show tasks')
    print('2. Add task')
    print('3. Remove task')
    print('4. Exit')
    print('5. Search tasks')

    choice = int(input('Enter your choice (1-4): '))
    
    if choice == 1:
        show_tasks()
    elif choice == 2:
        add_task()
    elif choice == 3:
        remove_task()
    elif choice == 5:
        search_tasks()
    elif choice == 4:
        return True
    else:
        print('Invalid choice. Please try again.')

def save_tasks():
    with open('todore.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def search_tasks():
    keyword = input('Enter a keyword to search for: ')
    keyword = keyword.strip().lower()
    found_tasks = [task for task in tasks if keyword in task.lower()]
    
    if found_tasks:
        print('Found tasks:')
        for task in found_tasks:
            print(f'- {task}')
    else:
        print('No tasks found with that keyword.')

while True:
    if  main_menu():
        save_tasks()
        break