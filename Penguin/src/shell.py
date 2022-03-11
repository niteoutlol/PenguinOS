import os
import socket

from colorama import Fore
from colorama import Style

from src.utils import cmdhandler

directory = str(os.getcwd())

hostname = str(socket.gethostname())

def thereareaccounts():
    accounts = len(os.listdir('./users/'))
    if accounts > 0:
        return True
    else:
        return False 

def shell(username, password):
    print()
    while thereareaccounts():
        raw = str(input(f'{Fore.GREEN}{username}@{hostname}{Style.RESET_ALL}:{Fore.BLUE}~{Style.RESET_ALL}$ '))
        cmdhandler.handle(raw, directory, username)

# Can be used for CONTROL + C keyboard interupts in future programs

# while True:
#     try:
#         print('in')
#     except KeyboardInterrupt:
#         print('Exit')
#         exit(1)