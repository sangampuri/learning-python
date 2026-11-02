tasks = []


def add_task():
    user_task = None
    while user_task != 'done':
        user_task = input('Enter a task: ')
        user_task = user_task.strip().lower()
        if user_task != 'done':
            tasks.append(user_task)
     


add_task()  

print('Your tasks: ')
for index,task in enumerate(tasks,1):
    print(f'{index}. {task}')

