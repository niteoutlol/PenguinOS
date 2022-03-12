import os
import shutil
import main
from src import setup
from colorama import Fore
from colorama import Style

from src import login

userspath = './users/'

prefix = f'{Fore.GREEN}[cmd]{Style.RESET_ALL}'

def handle(raw, dir, account):
    args = raw.split(' ') # this does contain the root command so args start at 1 args[1]++
    argint = len(args)
    if ' ' in raw:
        cmd = str(raw.split(' ')[0]).lower()
    else:
        cmd = str(raw).lower()

    if cmd == 'ls':
        # print(os.listdir(dir))
        files = os.listdir(dir)
        tosend = str('')
        for i in range(len(files)):
            tosend += f'{files[i]}  ' # Make folders blue and files gray / RESET_ALL
        print(tosend)
    elif cmd == 'rmusr' or cmd == 'delusr':
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
    elif cmd == 'mkusr':
        setup.setup()
    elif cmd == 'su':
       login.login()
    else:
        print(f'{cmd}: Command not found')