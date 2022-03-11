import os
from colorama import Fore
from colorama import Style
from getpass import getpass

from src import shell

prefix = f'{Fore.GREEN}[setup]{Style.RESET_ALL}'

def setup():
    print()
    ask = str(input('Create account? [Y/n] '))
    if ask.upper() == 'Y':
        username = str(input(f'{prefix} Account name: ').lower())
        password = str(getpass(f'{prefix} Account password: '))

        if ' ' in username:
            print(f'{prefix} Remove spaces from your account name')
            username = str(input(f'{prefix} Account name: ').lower())
        
        userfolder = str('./users/' + username + '/')
        if not os.path.exists('./users/'):
            os.mkdir('./users/')

        if not os.path.exists(userfolder):
            os.mkdir(userfolder)

        with open(userfolder + 'user', 'w') as f:
            f.write(password)

        print()
        print(f'{prefix} Account created')
        os.mkdir(f'{userfolder}home/')
        shell.shell(username, password)

    else:
        print(f'{prefix} Terminating')

