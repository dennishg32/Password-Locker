#!/usr/env python3.6
from User import User
from Credentials import Credential

def createuser(firstname, lastname, username, password):
  """
    function of create new user
  """
  newUser = User(firstname, lastname, username, password)
  return newUser

def saveUser(person):
  """
  function to save person or user
  """
  person.saveUser()
  
def allUser():
  """
    function to display all users
  """
  return User.allUser()

def createAccount(accountName, l_username, l_password):
  """
    function to create new account
  """
  newAccount = Credential(accountName, l_username, l_password)
  return newAccount

def saveAccount(creds):
  """
    saving account credential
  """
  creds.saveAccount()
  
def deleteAccount(creds):
  """
    delete account credential
  """
  creds.deleteAccount()
  
def findByusername(creds):
  """
    find account by username
  """
  return Credential.findByusername(creds)

def findAll():
  """
    display all account
  """
  return Credential.findAll()

def existingAccount(creds):
  """
    checks exist account credential
  """
  return Credential.existingAccount(creds)
  
def pwd_random(creds):
  """
    generating a random password
  """
  pwd = Credential.pwd_random()
  return pwd

def main():
  print('#'*25)
  print(" WELCOME TO PASSWORD LOCKER!!!!")
  print('#'*25)
  print('\n')
  print("Press :\n 0. To Create an account \n 1. To Login")
  print('='*25)
  code = input().lower()
  if code == '0':
    print('\n===============================')
    print("create your account")
    print('\n================================')
    fname = input('Firstname: ')
    lname = input('\n lastName: ')
    username = input('\n Username: ')
    while True:
      print('\n================================')
      print("Press: \n i. To choose Your password \n ii. To be generated password")
      print('\n================================')
      pwd= input().lower()
      if pwd == 'i':  
        password = input("Enter your password:  \n")
        break
      elif pwd == 'ii':  
        password = pwd_random()
        break
      else:
        print("wrong choice")
        
    saveUser(createuser(fname, lname, username, password))
    print('\n================================')
    print(f"Account has been create with username {username} and password {password}")
    print('\n================================')
    
  elif code == '1':
    print('\n================================')
    print("Welcome again!!!")
    username = input('username: ')
    pwd = input('\npassword: ')
    signin = existingAccount(username, pwd)
    if existingAccount == signin:
      print(f"Mr/s {username} its good to have u back")
      print('\n================================')
  
  while True:
    print('\n================================')
    print("\nPress\n dd. To display Accounts\n fa. To Find Account\n ga. To generate password\n dt. To delete\n e. To exit")
    print('\n================================')
    cd = input().lower()
    if cd == 'dd':
      if findAll():
        print('\n================================')
        print("List of accounts")
        print('\n================================')
        for acc in findAll():
          print(f"Account: {acc.accountName}\n Username: {username}\n Password: {password}")
          print('\n================================')
      else:    
        print("Please new Create Account")
        print('\n================================')
    elif cd == 'fa':
      print("Enter Your AccountName")
      print('\n================================')
      find = input().lower()
      if findByusername(find):
        creds = findByusername(find)
        print('\n================================')
        print(f"Account Name: {creds.accountName}")
        print('\n================================')
        print(f"Username: {creds.l_username}\nPassword: {creds.l_password} ")
        print('\n================================')
      else:
        print("Invalid Account")
        print('\n================================')
    elif cd == 'ga':
      pwd = pwd_random()
      print(f"{pwd} has been generated")
    
    elif cd == 'dt':
      print("Enter AccountName to delete")
      print('\n================================')
      find = input().lower()
      if findByusername(find):   
        creds = findByusername(find)
        print('\n================================')
        creds.deleteAccount()
        print(f"{creds.accountName} has been deleted!!")
        print('\n================================')
      else:
        print("Invalid Account")
    elif cd == 'e':
      print("byeee")
      break
    else:
      print("loadingggggggggggg..... try again later please")
      
if __name__ == "__main__":
  main()