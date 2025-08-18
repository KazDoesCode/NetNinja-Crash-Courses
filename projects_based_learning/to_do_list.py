def add_tasks(task:str,tasks:list):
    tasks.append(task)


def remove_tasks(index:int):
    tasks.pop(index)


def view_tasks(tasks:list):
    for i,task in enumerate(tasks, start = 1):
        print(f"Task {i}. {task}")


tasks = ['Do chores','Test','get out', 'go to the gym']
while True:
    try:
        print('Welcome to the to do list app please choose on of the options below: \n\n 1. Add task. \n\n 2.Remove task \n\n 3.View Task \n\n 4.Exit \n\n\n')
        choice = int(input('Choose an option from 1-4 \n'))
        if choice == '1':
            task = input("Enter the task: ")
            add_tasks(task,tasks)
        elif choice == '2':
            task_remove = int(input("Enter the index of the task to remove: "))
            view_tasks(tasks)
            remove_tasks(task_remove)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting... ")
            break
        else: print('Out of range, please choose a number from the list ( 1-4 ) ')
    except ValueError:
        print('Value error, please enter a number from the list ( 1-4 =) \n')