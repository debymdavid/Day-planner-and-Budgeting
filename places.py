import numpy as np
import csv
import random
import webbrowser
from budgeting import budg_sugg

f = open('Places to visit in Dubai.csv','r')
r = csv.reader(f)
location = {'Bur Dubai': ['Al Fahidi','Al Karama','Oud Metha','Al Safa','Jeddaf'],'Al Quoz':['Al Khail','Al Quoz','Al Barsha','Umm Suqeim'],'Downtown Dubai':['Downtown Dubai','Sheikh Zayed Road','Dubai Festival City'], 'Deira':['Al Warqa','Al Wasl','Deira','Umm Hurair'], 'Jumeirah':['Dubai Marina','Bluewater Islands','Palm Jumeirah'], 'Jebel Ali':['Jebel Ali','Southern Outskirts of Dubai']}

all_places = []
line = 0
for i in r:
    if line != 0:
        all_places.append(i)
    line += 1

def find(listOfPlaces):
    while len(listOfPlaces) < 5:
        place = random.choice(all_places)
        if place not in listOfPlaces:
            listOfPlaces.append(place)

# function to simplify the expression for time
def simplify(x):
    x = x.replace(':','.')
    x = x.split()
    x = list(filter(('-').__ne__, x))
    if 'and' in x:
      x = list(filter(('and').__ne__, x))
    for i in range(len(x)):
        j = float(x[i])
        x[i] = j
    if len(x) == 2:
      for i in range(2):
        x.append(0)
    return x

#finding places according to user's choice
def finding_places(area,act,money,time):
    temp = {7:[],6:[],5:[],3:[]}
    for i in all_places:
        c = 0
        if i[2] in location[area]:
            c +=3
            if i[1].upper() == act:
                c += 2
                if i[3][0].isdigit():
                        t = simplify(i[3])
                        if time not in np.arange(t[0],t[1]) or time not in np.arange(t[2],t[3]):
                         c += 1
                if i[5].isdigit():
                    if float(i[5]) <= money:
                        c += 1
                else:
                    c += 1
        if c in list(temp.keys()):
            temp[c].append(i)
    return temp

#presenting the best 5 options to the user
def best_five(temp):
    final_places = []
    for i in [7,6,5,3]:
        for j in temp[i]:
            final_places.append(j)
    if len(final_places) < 5:
            find(final_places)
    best = final_places[0:5]
    print('Places you can visit: ')
    count = 0
    while True:
        for i in range(5):
            print(i+1,'.',final_places[i][0])
        count += 1
        choice = eval(input('Enter the number of the place you want to visit, press any other num for new set of places: '))
        if choice in [1,2,3,4,5]:
            place = final_places[choice-1]
            break
        else:
            final_places = final_places[5::]
            if len(final_places) < 5:
                find(final_places)
            if count > 15:
                print('No more places left, since you are very indecisive a random place will be chosen for you according to your preferences. ')
                place = random.choice(best)
                print('The place you can visit today: ',place[0])
                break
    print("*"*120)
    print()
    return place 

def opening(final_place):  
    webbrowser.open_new(final_place[6])
    map=input("Open maps(y/n): ")
    if map.lower()=="y":
        webbrowser.open_new(final_place[7])

def main_places(username):
    print()
    flag = 'red'
    visited_places = []
    f = open('Places.csv','r')
    r = csv.reader(f)
    for i in r:
        if i[0] == username: 
            flag = 'green'
            visited_places.append(i[1])
    f.close()
    if flag == 'green':
        history = input('Do you want to visit a place that you have already visited (y/n): ')
        if history == 'y':
            for j in range(len(visited_places)):
                print(j+1,visited_places[j])
            opt = int(input('Enter the number of the place you want to visit: '))
            final_place = visited_places[opt-1]   
            x = input('Do you want to view the website of the place, enter (y or n): ')
            if x.lower() == 'y':
                opening(final_place)
        else:
            main(username)
    else:
        main(username)

def main(username):
    print("The areas available to visit:\n 1. Bur Dubai\n 2. Al Quoz\n 3. Downtown Dubai\n 4. Deira\n 5. Jumeirah\n 6. Jebel Ali")
    print()
    c = eval(input("Enter area number which is nearby you: ")) 
    area = list(location.keys())[c-1]
    print(area,"is chosen to visit!")
    print()
    act = input("Indoor or Outdoor, press any character for either options: ").upper()
    print()
    budget = eval(input('Maximum budget for the whole visit (incl entry fee,food,transport): '))
    money = eval(input("Maxium amount to be spent per person for entering the place : "))
    print()
    time = input("Time you want to visit in 24 hrs time: ")
    final_place = best_five(finding_places(area,act,money,time))
    x = input('Do you want to view the website of the place, enter (y or n): ')
    if x.lower() == 'y':
        opening(final_place)
    print()
    dict_budg = {}
    x = input('Do you want a budget for your visit enter(y or n): ').lower()
    if x == 'y':
        dict_budg= budg_sugg(budget,final_place)
    f = open('Places.csv','a',newline = '')
    w = csv.writer(f)
    w.writerow([username,final_place[0],dict_budg])
    f.close()