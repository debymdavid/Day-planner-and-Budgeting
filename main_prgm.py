from places import main_places
from budgeting import main_budget
from todo import main_todo   
from sql_part import main_sql

# Main program 
def main_act(username):
    print("Welcome to Plan Your Day!")
    print("We will help you decide what to do based on which day and time, place/region, budget, and activity you choose.")
    print("We also help you make a to-do list, and help manage your budget for various categories.")
    print()
    while True:
        print('*'*120)
        print()
        print('Choose any of the options below:')
        print('1.Find places to visit in Dubai')
        print('2.Make a to-do list')
        print('3.Manage your budget')
        print('4.Exit')
        print()
        c = int(input('enter your choice: '))
        if c == 1:
            main_places(username)
        elif c == 2:
            main_todo(username)
        elif c == 3:
            main_budget(username)
        else:
            print('*'*120)
            print('*'*120)
            main_sql(username)
            break 