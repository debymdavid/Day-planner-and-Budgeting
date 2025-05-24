import csv
import webbrowser
def opening():  
    f = open('Places to visit in Dubai.csv','r')
    r=csv.reader(f)
    place=input("Enter place to open website: ").lower()
    for i in r:
      if place==i[0].lower():
        webbrowser.open_new(i[6])
        print(i[6])
        map=input("Open maps(Yes/No): ")
        if map.lower()=="yes":
          webbrowser.open_new(i[7])
          print(i[7])
        else:
          break
