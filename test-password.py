import unittest
import pyperclip
from password import User


class TestUser(unittest.TestCase):
    '''
    Test class that define the test cases for user class behavior
    Arg:
    unittest.TestCase: helps in creating test cases.
    '''
    def setUp(self):
        '''
        Function to create a user account before each test
        '''
        self.new_user = User('Viv','Kimani', 'her1234')
        
    def test__init__(self):
        '''
        Test to check if the creation of user instances is done properly
        '''
        self.assertEqual(self.new_user.first_name, 'Viv')
        self.assertEqual(self.new_user.last_name, 'Kimani')
        self.assertEqual(self.new_user.password, 'her1234')
        
    def test_save_user(self):
        '''
        Check if the new user info are saved ino the user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
    
    
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases of the behaviors for the credential class.
    Args:
        unittest.TestCases: helps in creating test cases.
    '''
    
    def test_check_user(self):
        '''
        Function to test whether the login in function check_user works as expected.
        '''
        self.new_user = User('Viv','Kimani','her1234')
        self.new_user.save_user()
        user2 = User('Viv','Kimani','her1234')
        user2.save_user()
        
        for user in User.users_list:
            if user.first_name = user2.first_name and user.password = user2.password:
                current_user = user.first_name
        return current_user
    
        self.assertEqual(current_user, Credential.check_user(user1.password,user2.first_name))
        
    def setUp(self):
        '''
        Function to create an account's credentials before each test.
        '''
        self.new_credential = Credential('Viv', 'Twitter', 'test', 'her1234')
        
    def test__init__(self):
        '''
        Test to check whether the initialization of credential instances is done properly.
        '''
        self.assertEqual(self.new_credential.user_name, 'Viv')
        self.assertEqual(self.new_credential.site_name, 'Twitter')
        self.assertEqual(self.new_credential.account_name, 'test')
        self.assertEqual(self.new_credential.password, 'her1234')
        
    def test_save_credential(self):
        '''
        To check whether the new credentials info is saved in the credential list
        '''
        self.new_credential.save_credential()
        facebook = Credential('Viv','facebook','works!','her1234')
        facebook.save_credentials()
        self.assertEqual(len(Credential.credential_list), 2)
        
    def terDown(self):
        '''
        Function to clear the credential list after every test
        '''
        Credential.credentials_list=[]
        User.users_list=[]
        
    def test_display_credentials(self):
        '''
        Test to check if the display_credentials method, displays the correct credentials.
        '''
        self.new_credential.save_credentials()
        facebook = Credential('ray', 'facebook', 'works', 'her1234')
        facebook.save_credentials()
        gmail = Credential('Viv', 'Gmail', 'send', 'her4567')
        gmail.save_credentials()
        self.assertEqual(len(Credential.display_credentials(facebook.user_name)), 3)
        
    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_site_name method returns the correct credential.
        '''
        self.new_credential.save_credentials()
        facebook = Credential('Viv', 'facebook', 'works', 'her1234')
        facebook.save_credentials()
        credential_exists = Credential.find_by_site_name('facebook')
        self.assertEqual(credentials_exist, 'facebook')
        
    def test_copy_credentials(self):
        '''
        Test to check if the copy a credential method copies the correct credential
        '''
        self.new_credential.save_credentials()
        facebook = Credential('Viv', 'facebook', 'works', 'her1234')
        facebook.save_credentials()
        find_credential = None
        for credential in Credential.user_credentials_list:
            find_credential = Credential.find_by_site_name(
                credential.site_name)
            return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.site_name)
        self.assertEqual('pswd100', pyperclip.paste())
        print(pyperclip.paste())
        
        
        
        
if __name__ == '__main__':
    unittest.main()
