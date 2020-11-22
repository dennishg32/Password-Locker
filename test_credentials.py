import unittest
from unittest.main import main
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
  
  def test_init(self):
    """
      this function is all about initial save test them if are properly initializeed
    """
    self.assertEqual(self.newAccount.accountName, "Instagram")
    self.assertEqual(self.newAccount.l_username, "dennis_250")
    self.assertEqual(self.newAccount.l_password, "moringa01")

  def test_saveAccount(self):
    """
      this is about save account and test them using account list
    """
    self.newAccount.saveAccount()
    self.assertEqual(len(Credential.accountList),1)
  
  def tearDown(self):
    Credential.accountList = []
    
if __name__ == "__main__":
  unittest.main()
    
    