import os
from getpass import getpass
from src.utils.coloring import color

from src import shell

def setup():
    print()
    ask = str(input('Create account? [Y/n] '))
    if ask.upper() == 'Y':
        username = str(input(f'{color.FIELD.SETUP} Account name: ').lower())
        password = str(getpass(f'{color.FIELD.SETUP} Account password: '))

        if ' ' in username:
            print(f'{color.WARNING.SETUP} Remove spaces from your account name')
            username = str(input(f'{color.FIELD.SETUP} Account name: ').lower())

        userfolder = str('./users/' + username + '/')
        
        if os.path.exists(userfolder):
            print(f'{color.WARNING.SETUP} Account already exists')
            return

        if not os.path.exists('./users/'):
            os.mkdir('./users/')

        if not os.path.exists(userfolder):
            os.mkdir(userfolder)

        with open(userfolder + 'user', 'w') as f:
            f.write(password)

        print()
        print(f'{color.FIELD.SETUP} Account created')
        os.mkdir(f'{userfolder}home/')
        shell.shell(username, password, True)

    else:
        print(f'{color.WARNING.SETUP} Terminating')

