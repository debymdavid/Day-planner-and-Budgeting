#Finance and Budgeting section
import csv
import ast
import os
from prettytable import PrettyTable
lbudget = {} #budgeting
expense = {} #expenses

def budg_sugg(budget,final_place):
    efee = float(final_place[5])
    food = 0.20 *(budget - efee)
    transport = 0.15 * (budget-efee-food)
    extra = budget - (efee + food + transport)
    d_sugg = {'Place':final_place[0],'Entry fee':efee,'Food':food,'Transport':transport,'Extra':extra}
    print()
    print('The budget for your visit:')
    for i in d_sugg:
        print(i,d_sugg[i])
    return d_sugg

def get_both(username):
    global lbudget
    global expense
    f = open('budget_finance.csv','r')
    r = csv.reader(f)
    for i in r:
        if i[0] == username:
            lbudget = ast.literal_eval(i[1])
            expense = ast.literal_eval(i[2])
    f.close()

def save(username):
    f = open('budget_finance.csv','r')
    temp = open('newbudget_finance.csv','w',newline = "")
    r = csv.reader(f)
    w = csv.writer(temp)
    for i in r:
        if i[0] == username:
            w.writerow([username,lbudget,expense])
        else:
            w.writerow(i)
    f.close()
    temp.close()
    os.remove('budget_finance.csv')
    os.rename('newbudget_finance.csv','budget_finance.csv')

def create_budg():
    print()
    n=int(input("Enter no. of categories: "))
    for i in range(n):
        c=input("Enter category: ").upper()
        lbudget[c]=eval(input("Enter your budget for"+" "+c+" "": " ))
        print()
    
def enter_exp():
    for i in lbudget:
            expense[i]=eval(input("Enter expense for"+" "+i+" "+": "))
            print()

def new_cat():
    c=input("Enter the new category: ").upper()
    lbudget[c] = eval(input("Enter budget for"+" "+c+" "+":"))
    expense[c]=eval(input("Enter expense for"+" "+c+" "+": "))
    print()
        
def update_cat():
    c=input("Enter category to be updated: ").upper()
    if c not in list(lbudget.keys()):
        print('The category does not exist')
        return None
    y=int(input("""Do you want to update:
1. Budget
2. Expense
3. Both
Enter your choice: """))

    if y==1:
        lbudget[c]=eval(input("Enter updated budget for"+" "+c+" "+":"))
    elif y==2:
        expense[c]=eval(input("Enter updated expense for"+" "+c+" "+": "))
    elif y==3:
        lbudget[c]=eval(input("Enter updated budget for"+ " "+c+" "+": "))
        expense[c]=eval(input("Enter updated expense for"+" "+c+" "+": "))
    else:
        print("Enter a valid choice!")

def delete():
    c=input("Enter category to be deleted: ").upper()
    if c not in list(lbudget.keys()):
        print('The category does not exist')
        return None
    del lbudget[c]
    del expense[c]

def display():
    if lbudget == {}:
        print('Budget is empty')
        return None
    elif expense == {}:
        print('Expenses are not entered')
        return None
    t = PrettyTable(['Category', 'Budget', 'Expense','Remaining'])
    for i in lbudget:
        rem = lbudget[i]-expense[i]
        if rem < 0:
            r = "Over budget by "+str(rem*(-1))+" AED!"
            t.add_row([i,lbudget[i],expense[i],r])
        else:
            t.add_row([i,lbudget[i],expense[i],lbudget[i]-expense[i]])
    print(t)

def main_budget(username):
    global lbudget
    global expense
    while True:
        print("""Let's do the budgeting and track your expenses!
    1. Set budget for each category
    2. Enter expenses for each category 
    3. Set budget and expenses for a new category 
    4. Set new amount for a category 
    5. Delete a category
    6. Display budget and expenses
    7. Exit""")
        x= int(input("Select an option of your choice: "))
        if x==1:
            create_budg()
            f = open('budget_finance.csv','a',newline = "")
            w = csv.writer(f)
            w.writerow([username,lbudget,expense])
            f.close()
        elif x==2:
            f = open('budget_finance.csv','r')
            r = csv.reader(f)
            for i in r:
                if i[0] == username: 
                    lbudget = ast.literal_eval(i[1])
            f.close()
            enter_exp()
            save(username)
        elif x==3:
            get_both(username)
            new_cat()
            save(username)
        elif x==4:
            get_both(username)
            update_cat()
            save(username)
        elif x==5:
           get_both(username)
           delete()
           save(username)
        elif x==6:
            get_both(username)
            display()
        elif x==7:
            print('*'*120)
            break
        else:
            print("Enter a valid choice")