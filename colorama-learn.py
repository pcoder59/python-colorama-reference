import colorama

from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print("\nFore.RED : " + Fore.RED + "This Will Print Red Text\n")
print("This will be Red if autoreset is not True in init()\n")
print("\\033[39m or Fore.RESET :" + "\033[39m" + "This will Make Text Normal. Not Required if autoreset=True in init()\n")

print("Here is a list of Colours Supported By Colorama:\n")

"""Giving a Background of Black to all Except Black and Reset since Terminal Color can Differ"""

print(Back.WHITE + Fore.BLACK + "BLACK")
print(Back.BLACK + Fore.RED + "RED")
print(Back.BLACK + Fore.GREEN + "GREEN")
print(Back.BLACK + Fore.YELLOW + "YELLOW")
print(Back.BLACK + Fore.BLUE + "BLUE")
print(Back.BLACK + Fore.MAGENTA + "MAGENTA")
print(Back.BLACK + Fore.CYAN + "CYAN")
print(Back.BLACK + Fore.WHITE + "WHITE")
print(Fore.RESET + "RESET\n")

