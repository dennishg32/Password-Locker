class User:
  userList = []
  def __init__(self, fname, lname, username, pwd, pwd_conf):
    
    self.first_name = fname
    self.last_name = lname
    self.username = username
    self.password = pwd
    self.password_confirm = pwd_conf
    
  
    