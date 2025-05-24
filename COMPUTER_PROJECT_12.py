from acc_login import login
from acc_create import main_create

#Homepage  
while True:
    print('1.Login')
    print('2.Create account')
    print('3.Exit')
    x = eval(input('Enter choice: '))
    if x == 1:
        login()
    elif x == 2:
        main_create()
    else:
        print("Use our program again!")
        break       
    
