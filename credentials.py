import pyperclip

class Credentials:
    '''
    Class for credentials data
    '''
    credentials_list = []

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_credentials(self):
        '''adding new credentials to creddentials list'''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''remove credentials from the list'''
        Credentials.credentials_list.remove(self)


