import unittest
from Credentials import Credential

class TestAccount(unittest.TestCase):
  """
    Test class defines test cases for credentials class behaviours
    Args: 
      unittest.Testcase this class will helps creating cases
  """
  
  def setUp(self):
    """
      set up function to run before each test
    """
    self.newAccount = Credential(
      "Instagram", 
      "dennis_250", 
      "moringa01"
      )
    
    
    