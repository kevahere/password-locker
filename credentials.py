import pyperclip

class Credentials:
    '''
    Class for credentials data
    '''
    credentials_list = []

    def __init__(self,application,username,password):
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

    @classmethod
    def credentials_exist(cls,username):
        '''do these credentials exist?'''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list