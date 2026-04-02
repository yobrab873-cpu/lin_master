import math
import os
import subprocess

print("\033[H\033[2J", end="")

from colorama import Fore, Style, init
init(autoreset=True)

banner = subprocess.getoutput("figlet lin_Calc")

print(Fore.CYAN + banner)
print(Fore.BLUE + "=" * 60)

def main():
	is_running = True
	result = 0
	while is_running:
		banner = subprocess.getoutput("figlet lin_Calc")
		print(Fore.CYAN + banner)
		print(Fore.BLUE + "=" * 60)
		print(Fore.CYAN + " 1.Add \n 2.subtract \n 3.multiply \n 4.division \n 5.Exit")
		print("")
		choice = input("|> ")

		if choice == "5":
			print(Fore.RED  + "byeeeee")
			is_running = False
		elif choice == "1":
			pass

if __name__=="__main__":
	main()
