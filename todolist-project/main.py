#Lets start

import json 



def load_tasks():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        return tasks 

all_tasks = load_tasks()  

# print(all_tasks)

while True:

    print(''' 

    ===================== Welcome to TODO App ================================

    1) Add new task
    2) Display task
    3) Remove task
    4) Exit

    ===================== Welcome to TODO App ================================

    ''')

    user_choice = int(input("Enter your choice : "))

    if user_choice == 1:
        new_task = input("Enter the task : ")
        with open('tasks.json', 'w') as file:
            json.dump(new_task,file,indent=4)
    elif user_choice == 2:
        print("="*50)
        for task in all_tasks:
            for key,value in task.items():
                print(f"{key} : {value}")
    elif user_choice == 3: 
        remove_task = int(input("Enter ID to remove : "))
        all_tasks.remove(remove_task)
    elif user_choice == 4:
        break
    with open("tasks.json", 'w') as file:
        json.dump(all_tasks,file, indent=4)    


