class User:
    '''
    class that generates User objects and defines their behaviour
    '''

    user_list=[]
    def __init__(self,username,password):
        self.username = username
        self.password = password

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

