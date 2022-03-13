import os
import socket
import subprocess

from src.utils.coloring import color

from src.utils import cmdhandler

hostname = str(socket.gethostname())

def thereareaccounts():
    accounts = len(os.listdir('./users/'))
    if accounts > 0:
        return True
    else:
        return False 

directory = os.getcwd()
visualdirectory = '~'

def setdirectory(dir):
    directory = dir

def getdirectory(username):
    dir = directory
    return dir

def shell(username, password):
    print()
    directory = str(f'{str(os.getcwd())}/users/{username}/home/')
    while thereareaccounts():
        subprocess.call(['pyclean', './', '-q'])
        raw = str(input(f'{color.GREEN}{username}@{hostname}{color.TEXT}:{color.BLUE}~{color.TEXT}$ '))
        cmdhandler.handle(raw, directory, username, password)

# Can be used for CONTROL + C keyboard interupts in future programs

# while True:
#     try:
#         print('in')
#     except KeyboardInterrupt:
#         print('Exit')
#         exit(1)