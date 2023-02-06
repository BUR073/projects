import sqlite3
import base64

conn = sqlite3.connect('example.db')
c = conn.cursor()






#c.execute('''CREATE TABLE Users
            #(Id INT, UserName CHAR, Password CHAR, FailedAttempts INT, DisplayName CHAR)''')

conn.commit()





def checkUser(username, password): 
  
  

  c.execute("SELECT DisplayName, FailedAttempts FROM Users WHERE UserName = '"+username+"' AND Password = '"+password+"'")

  row = c.fetchone()
  print(row[0])
  print(row[1])
  DisplayName = row[0]
  FailedAttemps = row[1]

  

  if DisplayName != None: 

    UserNameExists = checkUsername(username)

    if UserNameExists == 1: 
    
      checkPassword(password)

    print("SYS: check failed attempts")
    NumFailed = checkfailed(username) 

      #print("Current Failed Attempts: ", NumFailed)

    if NumFailed > 3:
      print("Access Denied: To many failed attampts")

    elif UserNameExists == 0:
      print("Login Details not recognised")

    else:
      print("Please try again")

    

  

def checkfailed(username):
  c.execute("SELECT FailedAttempts FROM Users WHERE UserName = '"+username+"'")

  row = c.fetchone()
  print("SYS: Failed Attempts: ", row)

  new_failed = (''.join(map(str, row)))
  new_failed = (new_failed + 1)

  print("SYS: New failed as int", new_failed)


  c.execute("UPDATE Users SET FailedAttempts = '"+new_failed+"' WHERE UserName = '"+username+"'") 

  return(new_failed)





def checkUsername(username):

  c.execute("SELECT DisplayName, FailedAttempts FROM Users WHERE UserName = '"+username+"'")

  row = c.fetchone()
  print("checkUserName", row)
  
  if row == None:
    print("SYS: Username not found")
    return(0)
    

  else:
    print("SYS: Username found")
    return(1)

def checkPassword(password):
 

  

  c.execute("SELECT Username FROM Users WHERE Password = '"+password+"'")

  row = c.fetchone()
  print("CheckPassword", row[0])

  if row == None:
    print("Password is not found")
    return(0)

  else: 
    print("Password Found")
    return(0)




def NewID():
  c.execute("SELECT Id FROM Users")
  x = 0

  for row in c:
      id = (row[x])
      x = x +1 

  
  NewId = x + 1

  return NewId




def NewUser(NewUserName, NewPassword, NewDisplayName):
  
  #NewId = NewID()

  



  c.execute("INSERT INTO Users (UserName, Password, FailedAttempts, DisplayName) VALUES( ?, ?, ?, ?)", ( NewUserName, NewPassword, '0', NewDisplayName))

  conn.commit()

  print("Success")

def EnterNewUserDetails():

  print("Welcome")
  NewUsername = str(input("Enter new Username"))
  NewDisplayName = str(input("Please enter a Display Name: "))
  
  NewPassword = EnterPassword()

  NewUser(NewUsername, NewPassword, NewDisplayName)






def EnterPassword():
  print("")
  print("You Password must:")
  print("- Be More than 8 characters")
  print("- Include a number")
  print("- Include a symbol")
  print("- Include a Capital Letter")
  password = str(input("Please enter a password: "))

  GoodPassword = PasswordStrength(password)
  return(GoodPassword)





def PasswordStrength(password):
  
  if len(password) < 8 or password.lower() == password or password.upper() == password or password.isalnum()\
        or not any(i.isdigit() for i in password):
    print('Your password is weak, please enter a stronger one')
    EnterPassword()
  else:
    print('Your password is strong ')
    return(password)



NewUser('Username20', 'securepassword20', 'USERNAME20') 
checkUser('Username20', 'securepassword20') 
#EnterNewUserDetails()

conn.close()
 
 #c.execute("UPDATE Users set failedattempts = 0 where username = '"+username+"'")