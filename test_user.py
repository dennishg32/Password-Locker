import unittest
from user import User

class TestUser(unittest.Test):  
  
  def setUp(self):
    """
      set up method to run before when user intend to test each class
    """
    self.newUser = User("Dennis", "HG", "deHg", "kgl6", "kgl6")
