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
        self.new_user = User("Kevin","Ahere")

    def test_init(self):
        '''
        checking for proper initialization
        :return:
        '''
        self.assertEqual(self.new_user.first_name,"Kevin")
        self.assertEqual(self.new_user.last_name,"Ahere")

    def test_save_user(self):
        '''
        checking if oject is being correctly added
        :return:
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        '''
        emptys the list after running tests
        :return:
        '''
        User.user_list = []

    def test_delete_user(self):
        '''
        checking if users are deleted correctly
        :return:
        '''
        self.new_user.save_user()
        test_user = User("Kevinov","Aherestan")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user(self):
        self.new_user.save_user()
        test_user = User("Kevinov","Aherestan")
        test_user.save_user()

        found_user = User.find_user("Kevinov")

        self.assertEqual(found_user.last_name,test_user.last_name)

if __name__ == '__main__':
    unittest.main()