tasks = [ 
     'learn python',
    'practice django',
    'build a project',
]



def add_task():
    user_task = None
    while user_task != 'done':
        user_task = input('Enter a task: ')
        user_task = user_task.strip().lower()
        if user_task != 'done':
            tasks.append(user_task)

def view_tasks():
    print('Your tasks: ')
    for index,task in enumerate(tasks,1):
        print(f'{index}. {task}')
    

def delete_tasks():
    view_tasks()
    user_input = int(input('Enter the task number to delete:'))
    user_input = user_input-1
    del tasks[user_input]
    print('Task deleted successfully!')



def app_menu():
        print('===== TO-DO LIST APP =====')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Delete Task')
        print('4. Exit')
        choice = int(input('Enter your choice by number: '))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_tasks()
        elif choice == 4:
            print('Thanks for using the To-Do List App!')
            return True
        
        return False

while True:
   if app_menu():
       break


