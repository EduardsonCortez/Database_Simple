# Eduard Cortez Database Program with Colors
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

print("\n" + Fore.CYAN + "=" * 50)
print(Fore.YELLOW + "          DATABASE SYSTEM BY EDUARD CORTEZ       ")
print(Fore.CYAN + "=" * 50 + "\n")

# User Input
name = input(Fore.GREEN + "👉 Enter your name: ")
age = input(Fore.GREEN + "👉 Enter your age: ")
favhobby = input(Fore.GREEN + "👉 Enter your favorite hobby: ")

# Output Section
print("\n" + Fore.CYAN + "=" * 50)
print(Fore.MAGENTA + "📌 USER INFORMATION")
print(Fore.CYAN + "=" * 50)
print(Fore.BLUE + f"👤 Name           : {name}")
print(Fore.BLUE + f"🎂 Age            : {age}")
print(Fore.BLUE + f"🎯 Favorite Hobby : {favhobby}")
print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)
