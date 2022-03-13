import os
import shutil
import main
import shell

from src import setup
from src import login

userspath = './users/'

def list(dir):
    files = os.listdir(dir)
    tosend = str('')
    if not len(files) == 0:
        for i in range(len(files)):
            tosend += f'{files[i]}  ' # Make folders blue and files gray / RESET_ALL
        print(tosend)
    else:
        pass

def removeuser(argint, args, cmd, account):
    if argint >= 2:
        if ' ' in args[1] or args[1] == '':
            print(f'{cmd}: Argument cannot be empty')
        else:
            if os.path.exists(f'{userspath}{args[1]}/'):
                shutil.rmtree(f'{userspath}{args[1]}/')
                print(f'{cmd}: The {args[1]} account has been removed')
                if account == args[1]:
                    main.checkforusers()
            else:
                print(f'{cmd}: Account does not exist')
    else:
        print(f'{cmd}: Please supply necaserry arguments')

def createuser():
    setup.setup()

def switchuser():
    login.login()

def touch(argint, args, cmd, path):
    if argint >= 2:
        if ' ' in args[1] or args[1] == '':
            print(f'{cmd}: Argument cannot be empty')
        else:
            path += '/' + args[1]
            if os.path.exists(f'{path}'):
                print(f'{cmd}: The file already exists')
            else:
                with open(f'{path}', 'w') as f:
                    f.write('')
    else:
        print(f'{cmd}: Please supply necaserry arguments')

def createdirectory(argint, args, cmd, path):
    if argint >= 2:
        if ' ' in args[1] or args[1] == '':
            print(f'{cmd}: Argument cannot be empty')
        else:
            path += '/' + args[1]
            if os.path.exists(f'{path}'):
                print(f'{cmd}: The directory already exists')
            else:
                os.mkdir(f'{path}')
    else:
        print(f'{cmd}: Please supply necaserry arguments')

def remove(argint, args, cmd, path):
    try:
        if argint == 2:
            if ' ' in args[1] or args[1] == '':
                print(f'{cmd}: Argument cannot be empty')
            else:
                path += f'/{args[1]}'
                if os.path.exists(path):
                    os.remove(path)
                else:
                    print(f'{cmd}: File does not exist')
        elif argint == 3:
            # ITS A FOLDER!
            if ' ' in args[1] or args[1] == '' or ' ' in args[2] or args[2] == '':
                print(f'{cmd}: Argument cannot be empty')
            else:
                if args[1] == '-r':
                    path += f'/{args[2]}'
                    if os.path.exists(path):
                        os.rmdir(path)
                else:
                    print(f'{cmd}: Invalid argument')
        else:
            print(f'{cmd}: Please supply necaserry arguments')
    except Exception as ex:
        print(ex)

def changedirectory(argint, args, cmd, path):
    try:
        if argint >= 2:
            if ' ' in args[1] or args[1] == '':
                print(f'{cmd}: Argument cannot be empty')
            else:
                path += f'/{args[2]}'
                # change the directory within the shell module.
    except Exception as ex:
        print(ex)