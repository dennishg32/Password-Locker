import unittest
from user import User

class TestUser(unittest.TestCase):  
  
  def setUp(self):
    """
      set up method to run before when user intend to test each class
    """
    self.newUser = User(
      "Dennis",
      "HG",
      "deHg",
      "kgl6",
      "kgl6")
    
  def test_init(self):
    """
      test_init test case for object for initials
    """
    self.assertEqual(self.newUser.fname, "Dennis")
    self.assertEqual(self.newUser.lname, "HG")
    self.assertEqual(self.newUser.username, "deHg")
    self.assertEqual(self.newUser.pwd, "kgl6")
    self.assertEqual(self.newUser.pwd_conf, "kgl6")
    
  def test_saveUser(self):
    """
      this function is to check if user object saved in the user list
    """
    self.newUser.save_user()
    self.assertEqual(len(User.userList),1)

if __name__ == "__main__":
  unittest.main()
