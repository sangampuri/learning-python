
tasks = ['learn python', 'practice django', 'learn html','django python']

keyword = input('Enter a keyword: ')
keyword = keyword.strip().lower()

for task in tasks:
    if keyword in task:
        print(task)