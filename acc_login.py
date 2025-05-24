def decrypt(encrypted):
        l=['@','#','$','%','&','*','!','?']
        decrypted = ''
        start=0
        end=len(encrypted)
        while start<end:
            for i in range(start,end):
                if encrypted[i] in l:
                    temp = encrypted[start:i]
                    start=i+1
                    break
            bin1 = int(temp)
            den = 0
            i = 0
            while bin1!=0:
                r = bin1%10
                den += r*(2**i)
                bin1 = bin1//10
                i += 1
            char = chr(den)
            decrypted += char
        else:
            return decrypted
        
def login():
    import csv
    from main_prgm import main_act
    f=open("accounts.csv","r")
    r=csv.reader(f)
    #user interface for creating/accessing account 
    u=input("Enter username: ")
    count = 0
    flag = 'red'
    while count < 3:
        p=input("Enter password: ")
        line=0
        for i in r:
            if line!=0:
                if u==i[2] and p == decrypt(i[3]):
                    main_act(u)
                    flag = 'green'
                    break
            line+=1
        else:
            print("Incorrect username or password!")
            count += 1
        if flag == 'green':
            break
    else:
        print('Try again from beginning') 
    f.close()
