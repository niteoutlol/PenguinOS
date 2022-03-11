import os

def handle(cmd, dir):
    print(cmd)
    print(dir)
    if cmd.lower() == 'ls' or 'dir':
        print(os.listdir(dir))
    else:
        print(f'{cmd}: Command not found')
    pass