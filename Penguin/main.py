import os

from src import setup
from src import login
from src import shell

userdir = str('./users/')
if not os.path.exists(userdir):
    os.mkdir(userdir)

def checkforusers():
    if os.listdir(userdir):
        # There are existing users.
        login.login()
    else:
        # There are no existing users.
        setup.setup()

if __name__ == '__main__':
    checkforusers()