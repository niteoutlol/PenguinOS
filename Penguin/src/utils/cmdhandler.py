from src.utils.functions import *

userspath = './users/'

def handle(raw, dir, account, password):
    args = raw.split(' ') # this does contain the root command so args start at 1 args[1]++
    argint = len(args)
    if ' ' in raw:
        cmd = str(raw.split(' ')[0]).lower()
    else:
        cmd = str(raw).lower()

    if cmd == 'ls':
        list(dir)
    elif cmd == 'rmusr' or cmd == 'delusr':
        removeuser(argint, args, cmd, account)
    elif cmd == 'mkusr':
        createuser()
    elif cmd == 'su':
       switchuser()
    elif cmd == 'touch':
        path = dir
        touch(argint, args, cmd, path)
    elif cmd == 'rm':
        path = dir
        remove(argint, args, cmd, path)
    elif cmd == 'mkdir':
        path = dir
        createdirectory(argint, args, cmd, path)
    else:
        print(f'{cmd}: Command not found')