import os
from colorama import Fore
from colorama import Style
from getpass import getpass

from src import shell

prefix = f'{Fore.GREEN}[login]{Style.RESET_ALL}'

def checkusername(usernametocheck, usernamestocheckfrom):
    if not usernametocheck.lower() in usernamestocheckfrom:
        # The account does not exist
        print(f'{prefix} Account does not exist')
        print()
        
        return False
    else:
        # The account exists
        return True

def checkpassword(passwordtocheck, passwordtocheckfrom, account):
    if not passwordtocheck == passwordtocheckfrom:
        print(f'{prefix} Invalid password for {account}')
        print()

        return False
    else:
        return True
 
def login():
    accounts = os.listdir('./users/')
    print()
    account = str(input(f'{prefix} Account name: '))
    account = account.lower()
    while not checkusername(account, accounts):
        account = str(input(f'{prefix} Account name: '))
        account = account.lower()
    
    # The account exists

    password = str(getpass(f'{prefix} Enter password for {account}: '))

    accountfolder = str(f'./users/{account}/')
    acutalpassword = open (accountfolder + 'user', "r").read()
    while not checkpassword(password, acutalpassword, account):
        password = str(getpass(f'{prefix} Enter password for {account}: '))
    
    # Password is correct
    # login to the user
    print(f'{prefix} You are now logged into {account}')
    shell.shell(account, password)