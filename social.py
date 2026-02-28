import os
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)


def clear():
    os.system("clear")


def print_banner():
    """Display LIN_zPHISHER banner."""
    try:
        banner = subprocess.getoutput("figlet LIN_zPHISHER")
    except Exception:
        banner = "LIN_zPHISHER"

    print(Fore.YELLOW + Style.BRIGHT + banner)
    print(Fore.CYAN + "=" * 62)
    print(Fore.YELLOW + Style.BRIGHT + "                SOCIAL ENGINEERING MODULE")
    print(Fore.CYAN + "=" * 62)


def start():
	if os.path.isdir("zphisher"):
		print(Fore.GREEN +  "TOOL FOUND")

	else:
		print(Fore.GREEN + "INSTALLING SIMPLE PHISHING TOOL.")
		os.system("git clone https://github.com/htr-tech/zphisher.git")
		print(Fore.GREEN + "zphisher installed succeffull ✓")
	print("")
def act():
	print(Fore.YELLOW + "launching zphisher")
	os.chdir("/home/Lin_master/zphisher")
	print(Fore.RED + "This is for educational purposes and ethical hacking practise on maintained labs or authorized places")

	os.system("bash zphisher.sh")

def phishing():
    clear()
    print_banner()

    print(Fore.GREEN + "[1] Launch Phishing Framework")
    print(Fore.GREEN + "[2] Back to Main Menu")
    print(Fore.CYAN + "-" * 62)

    choice = input(Fore.YELLOW + "Select option > ")

    if choice == "1":
    	start()
    	act()
    elif choice == "2":
        return
    else:
        print(Fore.RED + "\n[!] Invalid selection.")

    input(Fore.YELLOW + "\nPress Enter to continue...")


if __name__ == "__main__":
    phishing()
