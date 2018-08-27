import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class for user behaviours
    '''

    def setUp(self):
        '''
        checking for proper user instantiation
        :return:
        '''
        self.new_user = User("kevahere","3nd0fday5")

    def test_init(self):
        '''
        checking for proper initialization
        :return:
        '''
        self.assertEqual(self.new_user.username,"kevahere")
        self.assertEqual(self.new_user.password,"3nd0fday5")

    def test_save_user(self):
        '''
        checking if oject is being correctly added
        :return:
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)