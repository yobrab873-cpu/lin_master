from colorama import Fore, Style, init
init(autoreset=True)

def help():
	print(Fore.GREEN +  "==================================================")
	print(Fore.YELLOW + "               LIN MASTER")
	print(Fore.CYAN +  "       Professional Linux Framework")
	print(Fore.GREEN + "--------------------------------------------------")
	print(Fore.CYAN + "       Version      : 1.0.0")
	print(Fore.CYAN + "       Release Year : 2026")
	print(Fore.CYAN + "       Author       : Brian Njuguna Mwangi")
	print(Fore.CYAN + "       License      : MIT")
	print(Fore.GREEN + "--------------------------------------------------")
	print(Fore.YELLOW + "       © 2026 LIN MASTER Project")
	print(Fore.YELLOW + "       Built for automation. Designed for dominance.")
	print(Fore.GREEN + "==================================================")
	print("")
	input(Fore.YELLOW + "PRESS ENTER TO CONTINUE")

print("")
if __name__=="__main__":
	help()

