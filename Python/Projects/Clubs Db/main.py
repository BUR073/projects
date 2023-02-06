import sqlite3
import names
import random 

conn = sqlite3.connect('example.db')
c = conn.cursor()






#c.execute('''CREATE TABLE Clubs
            #(Id INT, Name CHAR, Category CHAR, Primary Key (Id))''')

conn.commit()


def NewValues(id): 
  
  name = names.get_full_name()
  

  cat = random.randint(1,3)

  if cat == 1:
    category = ("Full")

  elif cat == 2:
    category = ("Student")

  elif cat == 3:
    category = ("Senior")
    
  new_details(id, name, category)




  
  


def new_details(Id, Name, Category):
  c.execute("Insert INTO Clubs (Id, Name, Category) values (?, ?, ?)", (Id, Name, Category))

  conn.commit() 





def printVal():
    f = open("myfile.txt", "a")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('''SELECT * FROM Clubs''')
    for r in c.fetchall():
        
        f.write(str(dict(r)) + "\n")



def create(lastId ,NumAddedVals ):
  

  
  while lastId < NumAddedVals: 
    NewValues(lastId)
    lastId = lastId + 1


#create(989816, 10184)
printVal() 


#conn.row_factory = sqlite3.Row
#c = conn.cursor()
#c.execute('''SELECT * FROM Clubs WHERE Name LIKE '%Burbridge' ''')
#for r in c.fetchall():
  #print(dict(r))

  








