import unittest
import pyperclip
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''runs before each test case'''
        self.new_credentials = Credentials("kevahere","3nd0fDay5")

    def test_init(self):
        self.assertEqual(self.new_credentials.username,"kevahere")
        self.assertEqual(self.new_credentials.password,"3nd0fDay5")

    def tearDown(self):
        Credentials.credentials_list = []

if __name__ == '__main__':
    unittest.main()
