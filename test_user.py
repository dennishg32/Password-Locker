import unittest
from User import User

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
    self.assertEqual(self.newUser.first_name, "Dennis")
    self.assertEqual(self.newUser.last_name, "HG")
    self.assertEqual(self.newUser.username, "deHg")
    self.assertEqual(self.newUser.password, "kgl6")
    self.assertEqual(self.newUser.password_confirm, "kgl6")
    
  def test_saveUser(self):
    """
      this function is to check if user object saved in the user list
    """
    self.newUser.saveUser()
    self.assertEqual(len(User.userList),1)
    
  def tearDown(self):
    User.userList = []

if __name__ == "__main__":
  unittest.main()
