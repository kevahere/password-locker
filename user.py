class User
    '''
    class that generates User objects and defines their behaviour
    '''

    user_list=[]

    def save_user(self):
        '''
        adds new users
        :return:
        '''
        User.user_list.append(self)

