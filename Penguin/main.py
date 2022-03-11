import os

from src import setup
from src import login
from src import shell

userdir = str('./users')

if os.listdir(userdir):
    # There are existing users.
    login.login()
else:
    # There are no existing users.
    setup.setup()
    login.login()