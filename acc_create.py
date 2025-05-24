import csv
import random
from main_prgm import main_act

accounts = open('accounts.csv','r')
r = csv.reader(accounts)
h = ['First name','Second name','Username','Password','Age']
def create_user():
    while True:
        username = input('Username: ').lower()
        if len(username) < 6:
            print('Minimum 6 characters required')
            continue
        for i in r:
            if i[2] == username:
                print('username already exists')
                break
        else:
            print('Username successfully created')
            return username
        accounts.close()
        print()

def create_pass():
    print('The password must contain at least 8 characters, 1 uppercase character, 1 number and 1 special character(no spaces).')
    while True:
        password = input('Password: ')
        if len(password) < 8:
            print('Minimum 8 characters required')
            pass
        acount = 0
        ncount = 0 
        scount = 0
        for i in password:
            if ord(i) in range(65,91):
                acount += 1
            elif i.isdigit():
                ncount += 1
            elif i.isalpha():
                pass
            else:
                scount += 1
        
        if (acount>0 and ncount>0 and scount>0) and len(password)>=8:
            print('Password is created')
            return password
        count =[acount,ncount,scount]
        for i in range(len(count)):
            if i == 0 and count[0] == 0:
                print('Password must contain at least one uppercase character')
            elif i == 1 and count[1] == 0:
                print('Password must contain at least one number')
            elif i == 2 and count[2] == 0:
                print('Password must contain at least one special character')
            
def encrypt(password):
    l=['@','#','$','%','&','*','!','?']
    passw=[]
    for i in password:
        passw.append(i)
    encrypted=""
    for i in passw:
        n=ord(i)
        binary=0
        p=0
        while n!=0:
            r = n%2
            binary = binary+r*10**p
            n=n//2
            p+=1
        code=random.randint(0,7)
        encrypted=encrypted+str(binary)+l[code]
    return(encrypted)

def main_create():
    print()
    print('*' * 100)
    print('Creating an account')
    first_name = input('Enter your first name: ')
    sec_name = input('Enter your second name: ')
    username = create_user()
    password = encrypt(create_pass())
    age = eval(input('Enter your age: '))
    cred = [first_name,sec_name,username,password,age]
    accounts = open('accounts.csv','a',newline = '')
    w = csv.writer(accounts)
    w.writerow(cred)
    accounts.close()
    print('Account created.')
    main_act(username)