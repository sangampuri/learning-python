tasks_list = []
tasks = ['Task 1', 'Task 2', 'Task 3', 'Task 4']

with open('D:\\sangam_codes\\Python\\projects\\tasks.txt', 'w') as file :
    for task in tasks:
        file.write(task+'\n')

