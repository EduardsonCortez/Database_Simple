# Eduard Cortez Database Program with Colors + Date/Time
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama
init(autoreset=True)

# Current Date & Time
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

print("\n" + Fore.CYAN + "=" * 60)
print(Fore.YELLOW + "          DATABASE SYSTEM BY EDUARD CORTEZ")
print(Fore.CYAN + "=" * 60)
print(Fore.GREEN + f"🕒 System Timestamp: {timestamp}")
print(Fore.CYAN + "=" * 60 + "\n")

# User Input
name = input(Fore.GREEN + "👉 Enter your name: ")
age = input(Fore.GREEN + "👉 Enter your age: ")
favhobby = input(Fore.GREEN + "👉 Enter your favorite hobby: ")

# Output Section
print("\n" + Fore.CYAN + "=" * 60)
print(Fore.MAGENTA + "📌 USER INFORMATION")
print(Fore.CYAN + "=" * 60)
print(Fore.BLUE + f"👤 Name           : {name}")
print(Fore.BLUE + f"🎂 Age            : {age}")
print(Fore.BLUE + f"🎯 Favorite Hobby : {favhobby}")
print(Fore.CYAN + "=" * 60)
print(Fore.GREEN + f"✅ Data recorded successfully at {timestamp}")
print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
