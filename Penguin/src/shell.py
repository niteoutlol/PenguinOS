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

class shell:
    global setdirectory
    global getdirectory

    def setdirectory(dir):
        global directory
        directory = dir
    
    def getdirectory():
        return directory
    
    def __init__(username, password, start: bool):
        global directory

        #directory = str(f'{str(os.getcwd())}/users/{username}/home')
        setdirectory(str(f'{str(os.getcwd())}/users/{username}/home'))
        if start:
            print()
            while thereareaccounts():
                osdic = getdirectory().split('/home')
                osdir = osdic[len(osdic) - 1]
                subprocess.call(['pyclean', './', '-q'])
                if getdirectory() == f'{str(os.getcwd())}/users/{username}/home':
                    raw = str(input(f'{color.GREEN}{username}@{hostname}{color.TEXT}:{color.BLUE}~{color.TEXT}$ '))
                else:
                    raw = str(input(f'{color.GREEN}{username}@{hostname}{color.TEXT}:{color.BLUE}~{osdir}{color.TEXT}$ '))
                cmdhandler.handle(raw, directory, username, password)
    


# Can be used for CONTROL + C keyboard interupts in future programs

# while True:
#     try:
#         print('in')
#     except KeyboardInterrupt:
#         print('Exit')
#         exit(1)