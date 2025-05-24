#to-do list
import ast
import csv
import os
global flag 
flag = 'red'
def display_list(todo_list):
    if not todo_list:
        print("The to-do list is empty.")
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")

def options(user_name):
    global flag
    f = open('todo.csv','r')
    r = csv.reader(f)
    for i in r:
        if i[0] == user_name: 
            todo_list = ast.literal_eval(i[1])
            flag = 'green'
            f.close()
            break
    else:
        todo_list=[]
    while True:
        print('*'*120)
        print()
        print("Options:")
        print("1. Display to-do list")
        print("2. Add task")
        print("3. Remove task")
        print("4. Save and Quit")
        choice = input("Enter the number of your choice: ")
        if choice=='1':
            display_list(todo_list)
        elif choice=='2':
            n = int(input('no of tasks to be added: '))
            for i in range(n):
                task=input("Enter the task: ")
                todo_list.append(task)
            print("Task(s) added.")
        elif choice=='3':
            display_list(todo_list)
            try:
                index=int(input("Enter the number of the task to remove: "))-1
                if 0<=index<len(todo_list):
                    removed_task=todo_list.pop(index)
                    print("Removed task: ",removed_task)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Enter a valid number.")
        elif choice == '4':
            if flag == 'green':
                f = open('todo.csv','r')
                r = csv.reader(f)
                new = open('newtodo.csv','w',newline = '')
                w = csv.writer(new)
                for i in r:
                    if i[0] == user_name:
                        w.writerow([user_name,todo_list])
                    else:
                        w.writerow(i)
                f.close()
                new.close()
                os.remove('todo.csv')
                os.rename('newtodo.csv','todo.csv')
                break
            else:
                f = open('todo.csv','a',newline = '')
                w = csv.writer(f)
                w.writerow([user_name,todo_list])
                f.close()
                break

        else:
            print("Invalid choice. Please select a valid option.")

def main_todo(user_name):
    choice=input("Do you want to make a to-do list (Yes/No): ")
    if choice.lower()=="yes":
        options(user_name)
    else:
        print("Okay!")
