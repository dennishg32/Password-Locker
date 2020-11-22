class User:
  userList = []
  def __init__(self, fname, lname, username, pwd, pwd_conf):
    
    """
     _init_ methods that help us define properties for our new user object
      Args:
          fname: New user first name 
          lname: New user last name 
          username: new Username
          pwd: New user password
          pwd_conf: New user password confirmation 
    """
    
    self.first_name = fname
    self.last_name = lname
    self.username = username
    self.password = pwd
    self.password_confirm = pwd_conf
    
  def saveUser (self):
    """
      this function saves user in user List
    """
    User.userList.append(self)
    
  
    