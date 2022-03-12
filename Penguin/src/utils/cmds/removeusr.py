userspath = './users/'

def command(cmd, argint, args, account):
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