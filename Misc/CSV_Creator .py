## Random CSV Creater
import barnum
from random import randint
import csv

number = int(input("Input:  "))
Id = 0

while number != 0:
    
    Name = barnum.create_name()


    Age = randint(1, 100)


    #Phone = barnum.create_phone()


    Email = barnum.create_email()

    Password = barnum.create_pw()


    Address = barnum.create_city_state_zip()


    credit_card = barnum.create_cc_number()

    Id = Id + 1



    complete = (Id, Name, Email, Age, Password, Address, credit_card)
    

    number = number - 1

    with open('CSV_FILE.csv', 'a', newline = '\n') as csvfile:
        my_writer = csv.writer(csvfile, delimiter = ',')
        my_writer.writerow(complete)

    


