from tinydb import TinyDB, Query
import pandas as pd
coins_database = {}




def select():
    
    print("What would you like to do?")
    print("1. Add to database")
    print("2. Remove from database")
    select = int(input("Input: "))

    if select == 1:
        insert() 

    elif select == 2:
        remove_database()






def remove_database():
    remove = str(input("Who would you like to remove?"))

    db.remove(remove)

    

    


def PayCalculator():

    db = TinyDB('db.json')

    name = str(input("Name: "))
    # Input name
    wage = int(input("Wage: "))
    # Input Wage

    wage2 = wage 
    
    money = {50 : "£50", 20 : "£20", 10 : "£10", 5 : "£5", 2 : "£2", 1 : "£1", 0.5 : "50p", 0.2 : "20p", 0.1 : "10p", 0.05 : "5p", 0.02 : "2p", 0.01 : "1p"}
    needed = {'£50': 0, '£20' : 0, '£10' : 0, '£5' : 0, '£2' : 0, '£1' : 0, '50p': 0, '20p': 0, '10p' : 0, '5p': 0, '2p': 0, '1p': 0}

    for coin in money:
        while wage  >= coin:
            needed[money[coin]] += 1
            wage -= coin
    db.insert({'name': name, 'coins' : needed })


def insert():
    rep = int(input("How many people would you like to enter?"))

    while rep != 0:
        PayCalculator()
        rep = rep - 1

 
    df_json = pd.read_json('db.json')
    df_json.to_excel('pay_numbers.xlsx')



            















##PayCalculator() 


                 
##for k,v in sorted(needed.items(), key=lambda x: x[1], reverse=True):
##    print(k,":", v)








select()
 
