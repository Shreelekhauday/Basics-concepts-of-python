password='shree@123'
attempts=3
while attempts >0:
    user_input=input('enter the password:')
    if user_input==password:
        print('Welcome')
        break
    else:
        attempts-=1
        if attempts >0:
            print('wrong password! You have {attempts} attempts left')
        else:
            print('account is blocked')
            break