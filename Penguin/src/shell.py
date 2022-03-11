import os
import socket

from colorama import Fore
from colorama import Style

from src.utils import cmdhandler

directory = str(os.getcwd())

hostname = str(socket.gethostname())

def shell(username, password):
    print()
    while True:
        raw = str(input(f'{Fore.GREEN}{username}@{hostname}{Style.RESET_ALL}:{Fore.BLUE}~{Style.RESET_ALL}$ '))
        cmdhandler.handle(raw, directory)
