import random
import pyperclip
class Credential:
  """
    creation of a class that will generates instances
  """
  accountList = []
  
  def __init__(self, accountName, l_username, l_password):
    """
      accountName : its name of account
      l_username : its user login name
      l_password: its user login password
    """
    self.accountName = accountName
    self.l_username = l_username
    self.l_password = l_password
  
  def saveAccount(self):
    """
      creates function for saving objects in account list
    """
    Credential.accountList.append(self)
    
  def deleteAccount(self):
    """
      function to delete account and test it
    """
    Credential.accountList.remove(self)
    
  @classmethod
  def findAll(cls):
    """
       functions to test all saved accounts
    """
    return cls.accountList
  
  @classmethod
  def findByusername(cls, account):
    """
      function to test account by user name
    """
    for user in cls.accountList:
      if user.accountName == account:
        return user
    
  @classmethod
  def copyPwd(cls, account):
    """
    """
    findAccount = Credential.findByusername(account)
    pyperclip.copy(findAccount.l_password)
    
  def pwd_random():
    """
    """
    password = random.randint([a,z],[0,9],[A,Z])
    return password
  
  @classmethod
  def existingAccount(cls, account):
    """
    """
    for acc in cls.accountList:
      if acc.accountName == account:
        return True
    return False