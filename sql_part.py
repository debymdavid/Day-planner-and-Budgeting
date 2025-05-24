import mysql.connector
import math
import datetime 
from pass_word import m_pass
from tkinter import *
from tkcalendar import DateEntry
from prettytable import PrettyTable
obj = mysql.connector.connect(host = 'localhost', password = m_pass, user = 'root')
s_date = ''

c = obj.cursor()
q = 'USE REVIEW;'
c.execute(q)

def get_review(username):
    q = 'SELECT SNO,USERNAME,STAR,FEEDBACK,DATEOFENTRY FROM REMARK;'
    c.execute(q)
    l = c.fetchall()
    num = len(l)
    rate = float(input('How many stars do you rate our program out of 5( enter a number in the range 1-5):'))
    feedback = input('Pls write your feedback about our project: ')
    today = datetime.date.today()
    q = 'INSERT INTO REMARK VALUES({},"{}",{},"{}","{}")'.format(num+1,username,rate,feedback,today)
    c.execute(q)
    l = c.fetchall()
    obj.commit()
    

def star(num):
    temp = ''
    for j in range(int(num)):
         temp += '★'
    dec = math.modf(num)[0]
    if dec >= 0.5:
        temp += '✬'
    if (5 - len(temp)) >= 1:
        for j in range(int(5-len(temp))):
            temp += '☆'
    return temp


def calendar():
    def get_date():
        global s_date
        s_date = cal.get()
        selected_date = cal.get()
        print(f"Selected date: {selected_date}")
    root = Tk()
    root.title('Calendar')
    root.geometry("250x250")
    cal = DateEntry(root, date_pattern="yyyy-mm-dd")
    cal.pack()
    btn = Button(root, text="Click Here To Return a Date ", command=get_date)
    btn.pack()
    root.mainloop()
    return s_date

def display():
    print()
    print('From which date do you want to view the reviews:')
    d = calendar() 
    q = 'SELECT * FROM REMARK WHERE DATEOFENTRY >= %s ORDER BY DATEOFENTRY DESC;'
    c.execute(q,(d,))
    l = c.fetchall()
    if l != []:
        t = PrettyTable(['SNO','USERNAME','RATINGS', 'FEEDBACK','DATEOFENTRY'])
        for i in l:
            rate = star(float(i[2]))
            t.add_row([i[0],i[1],rate,i[3],i[4]])
        print(t)
    else:
        print('No reviews after selected date')
    
def avg():
    print()
    q = 'SELECT AVG(STAR) FROM REMARK;'
    c.execute(q)
    l = c.fetchall()
    x = l[0][0]
    print('Avg rating of project:',star(x))

def del_review(username):
    print()
    q = 'SELECT * FROM REMARK WHERE USERNAME = %s'
    c.execute(q,(username,))
    l = c.fetchall()
    if l != []:
        t = PrettyTable(['SNO','USERNAME','RATINGS', 'FEEDBACK','DATEOFENTRY'])
        for i in l:
            rate = star(float(i[2]))
            t.add_row([i[0],i[1],rate,i[3],i[4]])
        print(t)
        sno_list = list(eval(input('Enter the SNO of the reviews to be deleted, separated by commas: ')))
        for i in range(len(sno_list)):
            q = 'DELETE FROM REMARK WHERE SNO = {}'.format(sno_list[i])
            c.execute(q)
            obj.commit()
        q = 'SELECT SNO FROM REMARK;'
        c.execute(q)
        l = c.fetchall()
        num = len(l)
        for i in range(num):
            q = 'UPDATE REMARK SET SNO = {} WHERE SNO = {}'.format(i+1,l[i][0])
            c.execute(q)
            obj.commit()
        return 'review(s) deleted'
    else:
        return 'no reviews found'

def main_sql(username):
    print('Thank you for using our program!')
    while True: 
        print()
        print('1.Rate the project and write a review')
        print('2.View other reviews of the project')
        print('3.View average rating of project')
        print('4.Delete a previous review')
        print('5.Exit')
        x = int(input('Enter your choice: '))
        if x == 1:
            get_review(username)
        elif x == 2:
            display()
        elif x == 3:
            avg()
        elif x == 4:
            print(del_review(username))
        else:
            c.close()
            obj.close()
            break
