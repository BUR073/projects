from tinydb import TinyDB, Query
import pandas as pd
from tkinter import *
from functools import partial

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
    
    def PayCalcSubFunc():
        db = TinyDB('db.json')
        db.insert({'name': name, 'coins' : needed })


    


    #window

    #name label and text entry box
    nameLabel = Label(tkWindow, text="Name").grid(row=0, column=0)
    name = StringVar()
    nameEntry = Entry(tkWindow, textvariable=name).grid(row=0, column=1)  

    #wagew label and wage entry box
    WageLabel = Label(tkWindow,text="Wage").grid(row=1, column=0)  
    wage = float()
    
    
    WageEntry = Entry(tkWindow, textvariable=wage).grid(row=1, column=1)
    WageEntry


    
    money = {50 : "£50", 20 : "£20", 10 : "£10", 5 : "£5", 2 : "£2", 1 : "£1", 0.5 : "50p", 0.2 : "20p", 0.1 : "10p", 0.05 : "5p", 0.02 : "2p", 0.01 : "1p"}
    needed = {'£50': 0, '£20' : 0, '£10' : 0, '£5' : 0, '£2' : 0, '£1' : 0, '50p': 0, '20p': 0, '10p' : 0, '5p': 0, '2p': 0, '1p': 0}

    for coin in money:
        while wage  >= coin:
            needed[money[coin]] += 1
            wage -= coin

    #EnterButton = Button(tkWindow,text=("Enter"),command=PayCalcSubFunc, grid(row=4, column=0))
    EnterButton = Tk.Button(main, text="Enter", command=partial(PayCalculatorSubFunc, name, needed))
    tkWindow.mainloop()

    


    


def insert():
    rep = int(input("How many people would you like to enter?"))

    while rep != 0:
        PayCalculator()
        rep = rep - 1

 
    df_json = pd.read_json('db.json')
    df_json.to_excel('pay_numbers.xlsx')



tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Cash Wage Calculator')








select()
 
