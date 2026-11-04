def load_tasks():
    with open('D:\\sangam_codes\\Python\\projects\\tasks.txt','r',) as file:
        tasks_list = file.read()
        tasks_list = tasks_list.split()
        for task in tasks_list:
            tasks.append(task)

tasks = [ ]
load_tasks()



def add_task():
    user_task = None
    while user_task != 'done':
        user_task = input('Enter a task: ')
        user_task = user_task.strip().lower()
        if user_task != 'done':
            tasks.append(user_task)
    save_tasks()

def view_tasks():
    print('Your tasks: ')
    for index,task in enumerate(tasks,1):
        print(f'{index}. {task}')
    

def delete_tasks():
    if not tasks:
        print('No tasks available!')
        return
    view_tasks()
    user_input = int(input('Enter the task number to delete:'))
    user_input = user_input-1
    if user_input >= 0 and user_input < len(tasks):
        del tasks[user_input]
        print('Task deleted successfully!')
        save_tasks()

    else:
        print('Invalid task number')



def app_menu():
        print('===== TO-DO LIST APP =====')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Delete Task')
        print('4. Exit')
        print('5. Search')
        choice = int(input('Enter your choice by number: '))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_tasks()
        elif choice == 5:
            search_tasks()
        
        elif choice == 4:
            print('Thanks for using the To-Do List App!')
            return True

        return False

def save_tasks():
    with open('D:\\sangam_codes\\Python\\projects\\tasks.txt','w') as file:
        for task in tasks:
            file.write(task+'\n')

def search_tasks():
    keyword = input('Enter a keyword: ')
    keyword = keyword.strip().lower()
    found = False
    for task in tasks:
        if keyword in task:
            found = True
            print(task)

    if not found:
        print('Task not found')





while True:
    
   if app_menu():
     
       break


