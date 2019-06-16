#!usr/bin/python3
import datetime
name = input("Enter your name: ")
age=int(input("Enter your age: "))
now=datetime.datetime.now()
print(name +' will turn 95 bt the year: ', ((95-age)+now.year))
