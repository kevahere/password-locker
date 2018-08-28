#!/usr/bin/env python3.6
from credentials import Credentials
from user import User
from random import *
import string

def create_user(first_name, last_name):
    ''' Function to create a user'''
    new_user = User(first_name, last_name)
    return new_user
def create_credential(app_name,username,password):
    new_credential = Credentials(app_name,username,password)
    return  new_credential
def save_users(user):
    '''Function to save a user'''
    user.save_user()
def generate_password():
    '''Function to generate a new password'''
    min_char = 6
    max_char = 12
    allchar = string.ascii_letters + string.punctuation + string.digits
    pwd = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return pwd
def save_credential(new_credential):
    Credentials.save_credentials(new_credential)
def main():
    username = input("Enter ")
    app_name =input("Enter ")
    password = generate_password()
    save_credential(create_credential(app_name,username,password))
    print ("Your new password is: ", password)
    display = Credentials.display_credentials()
    print (display.application)
if __name__ == '__main__':
    main()

