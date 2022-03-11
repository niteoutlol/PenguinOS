import os
from colorama import Fore
from colorama import Style

from src import shell

accounts = os.listdir('./users/')

prefix = f'{Fore.GREEN}[login]{Style.RESET_ALL}'

def login():
    print()
    account = str(input(f'{prefix} Account name: '))
    account = account.lower()
    if not account.lower() in accounts:
        # The account does not exists
        print(f'{prefix} Account does not exist')
        print()
        account = str(input(f'{prefix} Account name: '))
        account = account.lower()
    
    # The account exists

    password = str(input(f'{prefix} Enter password for {account}: '))

    accountfolder = str(f'./users/{account}/')
    acutalpassword = open (accountfolder + 'user', "r").read()
    acutalpassword.close()
    if not acutalpassword == password:
        print(f'{prefix} Invalid password for {account}')
        print()
        password = str(input(f'{prefix} Enter password for {account}: '))
    
    # Password is correct
    # login to the user
    print()
    print(f'{prefix} You are now logged into {account}')
    shell.shell(account, password)