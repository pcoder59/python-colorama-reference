import colorama

from colorama import Fore, Back, Style

colorama.init()

print("Fore.RED: " + Fore.RED + "This Will Print Red Text")
print("This will be Red if autoreset is not True in init()")
print("\033[39m")