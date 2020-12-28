import colorama

from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print("\nFore.RED : " + Fore.RED + "This Will Print Red Text\n")
print("This will be Red if autoreset is not True in init()\n")
print("\\033[39m or Fore.RESET :" + "\033[39m" + "This will Make Text Normal. Not Required if autoreset=True in init()\n")

print("Here is a list of Colours Supported By Colorama:\n")

"""Giving a Background of Black to all Except Black and Reset since Terminal Color can Differ"""

print("Fore.BLACK " + Back.WHITE + Fore.BLACK + "BLACK")
print("Fore.RED " + Back.BLACK + Fore.RED + "RED")
print("Fore.GREEN " + Back.BLACK + Fore.GREEN + "GREEN")
print("Fore.YELLOW " + Back.BLACK + Fore.YELLOW + "YELLOW")
print("Fore.BLUE " + Back.BLACK + Fore.BLUE + "BLUE")
print("Fore.MAGENTA " + Back.BLACK + Fore.MAGENTA + "MAGENTA")
print("Fore.CYAN " + Back.BLACK + Fore.CYAN + "CYAN")
print("Fore.WHITE " + Back.BLACK + Fore.WHITE + "WHITE")
print("Fore.RESET " + Fore.RESET + "RESET\n")

print("Here is a list of Highlights Supported by Colorama:\n")

"""Text Color Set to Black For Everything Except Black and Reset"""

print("Back.BLACK " + Back.BLACK + Fore.WHITE + "BLACK")
print("Back.RED " + Back.RED + Fore.BLACK + "RED")
print("Back.GREEN " + Back.GREEN + Fore.BLACK + "GREEN")
print("Back.YELLOW " + Back.YELLOW + Fore.BLACK + "YELLOW")
print("Back.BLUE " + Back.BLUE + Fore.BLACK + "BLUE")
print("Back.MAGENTA " + Back.MAGENTA + Fore.BLACK + "MAGENTA")
print("Back.CYAN " + Back.CYAN + Fore.BLACK + "CYAN")
print("Back.WHITE " + Back.WHITE + Fore.BLACK + "WHITE")
print("Back.RESET " + Back.RESET + "RESET\n")

print("Here is a list of Style Supported By Colorama:\n")

print("Style.DIM " + Style.DIM + "DIM")
print("Style.NORMAL " + Style.NORMAL + "NORMAL")
print("Style.BRIGHT " + Style.BRIGHT + "BRIGHT")
print("Style.RESET_ALL " + Style.RESET_ALL + "'RESET ALL STYLES'")