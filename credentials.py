import pyperclip
import string
from random import *

class Credentials:
    '''
    Class for credentials data
    '''
    credentials_list = []

    def __init__(self, application, username, password):
        self.application = application
        self.username = username
        self.password = password

    def save_credentials(self):
        '''adding new credentials to creddentials list'''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''remove credentials from the list'''
        Credentials.credentials_list.remove(self)
        # error (ValueError: list.remove(x): x not in list)

    def generate_password(self):
        '''Function to generate a new password'''
        min_char = 6
        max_char = 12
        allchar = string.ascii_letters + string.punctuation + string.digits
        pwd= "".join(choice(allchar) for x in range(randint(min_char, max_char)))
        print ("Your new password is: ")


    @classmethod
    def credentials_exist(cls, username):
        '''do these credentials exist?'''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        for cred in cls.credentials_list:
            return cred

    @classmethod
    def copy_creds(cls ,username):
        creds_to_copy = Credentials.find_by_username(username)
        pyperclip.copy(creds_to_copy)

''' End of Class'''