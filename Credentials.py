
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
    
  