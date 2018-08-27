class User:
    '''
    class that generates User objects and defines their behaviour
    '''

    user_list=[]
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def save_user(self):
        '''
        adds new users
        :return:
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        removes users
        :return:
        '''
        User.user_list.remove(self)

    @classmethod
    def find_user(cls,first_name):
        for user in cls.user_list:
            if user.first_name == first_name:
                return user