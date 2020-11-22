import unittest
from unittest.main import main
from Credentials import Credential
import pyperclip

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
    
  def test_saveMoreAccount(self):
    """
     this function helps us to save more than one account and test them
    """
    self.newAccount.saveAccount()
    testAccount = Credential(
      "facebook",
      "hernandez",
      "moringa02"
    )
    testAccount.saveAccount()
    self.assertEqual(len(Credential.accountList),2)
    
    
  def deleteAccountTest(self):
    """
      this function delete account check if test has passed from account list
    """
    self.newAccount.saveAccount()
    testAccount = Credential(
      "Twitter",
      "dennishg250",
      "moriinga03")
    testAccount.saveAccount()
    self.newAccount.deleteAccount()
    self.assertEqual(len(Credential.accountList),1)
  
  def copypasswordTest(self):
    """
      this functions helps to copy password and test if it was successfully copied on clipboard
    """
    self.newAccount.saveAccount()
    Credential.copyPwd('moriinga03')
    self.assertEqual(self.newAccount.l_password, pyperclip.paste())
  
  def randomPwdGenerate(self):
    """
      Function to generate random password
    """
    random = Credential.pwd_random()
    self.assertTrue(random)
    
  def findallTest(self):
    """
      Function to test if we can find all accounts registered
    """
    self.assertEqual(Credential.findAll(), Credential.accountList)
    
  def testCheckExistingAccount(self):
    """
      Function to test and check if account exist or not
    """
    self.newAccount.saveAccount()
    testAccount = Credential(
      "Ayoba",
      "deno",
      "dano"
    )
    testAccount.saveAccount()
    existingAccount = Credential.existingAccount("Ayoba")
    self.assertTrue(existingAccount)
  
  def findByUsername(self):
    """
      function to test account by username
    """
    self.newAccount.saveAccount()
    testAccount = Credential(
      "Pinterest",
      "Dennis Hg"
      "momo05"
    )
    testAccount.saveAccount()
    findbyUsername = Credential.findByuser()
    self.assertEqual(findbyUsername.l_username. testAccount.l_username)
    
  
    
    
    
    
if __name__ == "__main__":
  unittest.main()
    
    