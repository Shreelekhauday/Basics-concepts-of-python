class User:
    def __init__(self, username, password='shree@123'):
        self._username = username
        self._password = password


    def check_password(self,password):
        return self._password==password

    def change_password(self, new_password):
        self._password =new_password
        print('password changed successfully!')

    def get_username(self):
        return self._username


#if _name_ == "_main_":
username = input("Enter your username: ")
user = User(username)
password = input("Enter your password: ")

if user.check_password(password):
    print('Welcome, {}!'.format(user.get_username()))
else:
    print('Password incorrect.')
    change_option=input('Do you wnat to change your password?(yes/no):').lower()
    if change_option=='yes':
        new_password=input('Enter your new password:')
        user.change_password(new_password)
    else:
        print('Goodbye!')