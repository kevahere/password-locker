#!/usr/bin/env python3.6
from credentials import Credentials
from user import User

def create_user(first_name, last_name):
    ''' Function to create a user'''
    new_user = User(first_name, last_name)
    return new_user





if __name__ == '__main__':
    main()