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
    view_tasks()

     
delete_tasks()

