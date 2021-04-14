import string
import random
import pyperclip

#Class variables
#Global variable



class User:
    
    '''
    A class to create and save user accounts and their information
    '''
    
    # Class Variables
    # global users_list
    
    users_list = []

    def __init__(self, first_name, last_name, password):
        '''
        Method to define the properties that each object will hold.
        '''

        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        Function to save a newly created user instance
        '''
        User.users_list.append(self)
        
    @classmethod
    def verify_user(cls, first_name, password):
        for user in cls.users_list:
            return (first_name == user.first_name) and (password == user.password)


class Credential:
    
    '''
    Class to create  account credentials, generate passwords and save their information
    '''
    # Class Variables
    credentials_list = []
    user_credentials_list = []
    
    @classmethod
    def check_user(cls, first_name, password):
    
        '''
        Method that checks if the name and password entered match entries in the users_list
        '''
        
        current_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user

    def __init__(self, user_name, site_name, account_name, password):
        '''
        Method to define the properties that each user object will hold.
        '''

        # instance variables
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        Function to save a newly created user instance
        '''
        # global users_list
        Credential.credentials_list.append(self)
    
    @classmethod
    def generate_password(cls, size):
        '''
        Function to generate an 9 character password for a credential
        '''
        char=string.ascii_uppercase+string.ascii_lowercase+string.digits
        gen_pass = ''.join(random.choice(char) for _ in range(size))
        return gen_pass

    @classmethod
    def display_credentials(cls, user_name):
        '''
    A class method to display the list of credentials saved
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        A method that takes in a site_name and returns a credential that matches that site_name.
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential

    
    @classmethod
    def copy_credential(cls, site_name):
        '''
        A class method that copies a credential's info after the credential's site name is entered
        '''
        find_credential = Credential.find_by_site_name(site_name)
        
        return pyperclip.copy(find_credential.password)
        