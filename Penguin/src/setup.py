import os

def setup():
    print()
    ask = str(input('Create account? (Y/n) '))
    if ask.upper() == 'Y':
        username = str(input('[setup] Account name: ').lower())
        password = str(input('[setup] Account password: '))

        if ' ' in username:
            print('[error] Remove spaces from your account name')
            username = str(input('[setup] Account name: ').lower())
        
        userfolder = str('./users/' + username + '/')

        os.mkdir(userfolder)

        with open(userfolder + 'user', 'w') as f:
            f.write(password)

        print('[setup] Account created')

    else:
        print('Terminating')
        exit(0)

