class User:
  userList = []
  def __init__(self, fname, lname, pwd, pwd_conf):
    
    self.first_name = fname
    self.last_name = lname
    self.password = pwd
    self.password_confirm = pwd_conf
    
  
    