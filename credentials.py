import pyperclip

class Credentials:
    '''
    Class for credentials data
    '''
    credentials_list = []

    def __init__(self,username,password):
        self.username = username
        self.password = password
