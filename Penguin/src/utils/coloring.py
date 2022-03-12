from colorama import Fore
from colorama import Style

# def color(msg: str, color: str):
#     if color is None:
#         return f'{}'

class color:
    TEXT = f'{Style.RESET_ALL}'
    BLUE = f'{Fore.BLUE}'
    YELLOW = f'{Fore.YELLOW}'
    RED = f'{Fore.RED}'
    GREEN = f'{Fore.GREEN}'
    class WARNING:
        LOGIN = f'{Fore.RED}[login]{Style.RESET_ALL}'
        SETUP = f'{Fore.RED}[setup]{Style.RESET_ALL}'
        CMD = f'{Fore.RED}[cmd]{Style.RESET_ALL}'
    class FIELD:
        LOGIN = f'{Fore.GREEN}[login]{Style.RESET_ALL}'
        SETUP = f'{Fore.GREEN}[setup]{Style.RESET_ALL}'
        CMD = f'{Fore.GREEN}[cmd]{Style.RESET_ALL}'