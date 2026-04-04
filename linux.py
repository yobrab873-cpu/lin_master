import ping_host
import port_scan
import helper
import os
import time
import subprocess
import social

from apps import search, calculator, games

def clear():
	os.system("clear")

clear()

#-----------------------done---------------------#



from colorama import Fore, Style, init
init(autoreset=True)

init()

banner = subprocess.getoutput("figlet LIN_MASTER")
print(Fore.GREEN + Style.BRIGHT + banner)

print(Fore.CYAN + "--------------------------------------------------")
print(Fore.MAGENTA + Style.BRIGHT + "WELCOME TO LINUX HELPER")
print(Fore.CYAN + "----------------------------------------[v1.0.0]----")
print(Fore.CYAN + "Developed by [BRIAN NJUGUNA™] (©2026)")
print("")

print(Fore.GREEN + "loading.....")
time.sleep(0.2)

#--------main loop--------------#
running = True


#----------------PORT SCANNING FUNCTION---------------#
def dev():
	print(Fore.MAGENTA + "while adavancing this tool make sure you have a backup file: \n \n Do you want to continue \n yes \n no")
	sur = input(": "). lower()
	if sur == "y" or sur == "yes":

		os.system("nano /home/lin_master/linux.py")



def port_scanner():
	clear()
	banner = subprocess.getoutput("figlet LIN_PORT SCANNER")
	print(Fore.YELLOW + Style.BRIGHT + banner)

	input("press enter to continue")
#---------WEB EXPLOITATION FUNCTION--------------------#
def web():
	clear()
	banner = subprocess.getoutput("figlet LIN_WEB EXPLOITER")
	print(Fore.YELLOW + Style.BRIGHT + banner)
	os.system("bash web_exploiter.sh")
	input(Fore.YELLOW + "press enter to continue")


#------------------------system updator-------------------------#
def upd():
	clear()
	banner = ("Updating system")
	print(Fore.YELLOW + Style.BRIGHT + banner)
	os.system("bash .upd.sh")
	print(Fore.GREEN + "system is up to date")
	print("")
	input(Fore.YELLOW + "press enter to continue")

#--------------------------package installer-----------------------#
def new():
	clear()
	banner = subprocess.getoutput("figlet PACKAGES")
	print(Fore.YELLOW + Style.BRIGHT + banner)
	package = input("Enter package name: ")
	print(f"installing {package}")
	result = subprocess.getoutput(f"sudo apt install {package} -y")
	print("process finished")
	input(Fore.GREEN + "press enter to continue: ")
	print("")

#-----------------------------file creator---------------------------#
def new_file():
	clear()
	banner = subprocess.getoutput("figlet LIN_FILE CREATOR")
	print(Fore.YELLOW + Style.BRIGHT + banner)
	print("")
	print(Fore.BLUE + "MENU")
	print(Fore.YELLOW + "1. Create dir")
	print(Fore.YELLOW + "2. Create file")

	opt = input(": \n")
	if opt == "1":
		print(Fore.BLUE + "loading directories.......")
		time.sleep(1)
		print(Fore.YELLOW + "--------------------------------------------------------------------------")
		dir_name = input(Fore.YELLOW + "enter dir name\n")
		print(Fore.GREEN + "creating directory....")


		if os.path.isdir(dir_name):
			print(Fore.RED + "[+] Apache directory found")
			print(Fore.YELLOW + "X directory already exists")
			input(Fore.GREEN + "press enter to continue: ")
			print("")


		else:
			print(Fore.GREEN + "[✓] Apache directory is being created")
			os.mkdir(dir_name)
			print(Fore.GREEN + (f"directory {dir_name} created ✓"))
			input(Fore.YELLOW + "press enter to continue")

	elif opt == "2":
		print(Fore.BLUE + "loading files")
		time.sleep(1)
		print(Fore.YELLOW + "-----------------------------------------------------------------")
		file_name = input(Fore.YELLOW + "enter new file name or path\n")
		print(Fore.GREEN + "optimizing........")

		if os.path.isfile(file_name):
			print(Fore.RED + "x file already exists")
			input(Fore.RED + "press enter to continue")
			print("")
		else:
			print(Fore.GREEN + "creating file")
			os.system(f"touch {file_name}")
			print(Fore.GREEN + f"file {file_name} created")
			print("")
			input(Fore.GREEN + "press enter to continue: ")
			print("")
def ent():
	print(Fore.BLUE + "<" + "=" * 20 + ">")
	banner = subprocess.getoutput("figlet LIN_GAMES")
	print(Fore.YELLOW + banner)
	print(Fore.BLUE + "<" + "=" * 20 + ">")
	print(Fore.YELLOW + "1. Number ninja \n2. Rock Paper x")
	choice = input(": ")
	if choice == "1":
		games.number_ninja()

#-----------------------learn-----------------------------#
def commands():
	clear()
	banner = subprocess.getoutput("figlet LIN_COMMANDS")
	print(Fore.YELLOW + Style.BRIGHT + banner)
	input(Fore.GREEN + "press enter to continue: ")
	print("")

#-------------------------moreapps------------------#
def more_apps():
	print(Fore.CYAN + "<" + "=" * 50 + ">")
	banner = subprocess.getoutput("figlet LIN_MASTER")
	print(Fore.GREEN + Style.BRIGHT + banner)
	print(Fore.CYAN + "--------------------------------------------------")
	print(Fore.MAGENTA + Style.BRIGHT + "WELCOME TO LINUX HELPER")
	print(Fore.CYAN + "----------------------------------------[v1.0.0]--")
	print(Fore.CYAN + "Developed by [BRIAN NJUGUNA™] (©2026)")
	print("")
	print(Fore.YELLOW + "----------------MENU------------------")
	print("")

	print(Fore.MAGENTA + """
	|
        |  0. ....                                       |
        |  1. Lin Dictionary                             |
        |  2. Calculator                                 |
        |  3. N/A                                        |
        |  4. N/A                                        |
        |  5. N/A                                        |
        |  6. N/A                                        |
        |  7. N/A                                        |
        |  8. N/A                                        |
        |  9. N/A                                        |
        | 10. N/A                                        |
        | 11. N/A                                        |
        |                                                |
        | 98. Exit                                       |
        | 99. clear screen                               |
	""")
	user_ch = input("--\n ")
	match user_ch:
		case "1":
			search.lin_dict()

		case "2":
			calculator.main()

		case _:
			print(Fore.RED + "invalid user choice")
#-------------------MENU----------------------------#
while running:


	print(Fore.CYAN + "<" + "=" * 50 + ">")
	banner = subprocess.getoutput("figlet LIN_MASTER")
	print(Fore.GREEN + Style.BRIGHT + banner)

	print(Fore.CYAN + "--------------------------------------------------")
	print(Fore.MAGENTA + Style.BRIGHT + "WELCOME TO LINUX HELPER")
	print(Fore.CYAN + "----------------------------------------[v1.0.0]--")
	print(Fore.CYAN + "Developed by [BRIAN NJUGUNA™] (©2026)")
	print("")
	print(Fore.YELLOW + "----------------MENU------------------")
	print("")

	print(Fore.MAGENTA + """
	|
	|  0. Develop linux master			 |
	|  1. Port scanning				 |
	|  2. Web exploitation				 |
	|  3. Phishing					 |
	|  4. Update system				 |
	|  5. Install package				 |
	|  6. Create files and Directories		 |
	|  7. Learn commands				 |
	|  8. Help					 |
	|  9. Games					 |
	| 10. Host enumaration				 |
	| 11. More apps               			 |
        |         					 |
	| 98. Exit		 			 |
	| 99. clear screen                               |
	""")
	print(Fore.YELLOW + "-----------------------------------------")
	print("Choose from menu")
	choice = input(": ")
	match choice:
		case "99":
			 clear()

		case "0":
			clear()
			dev()
		case "9":
			ent()

		case "1":
			port_scanner()
			port_scan.main()

		case "2":
			web()

		case "3":
			social.phishing()

		case "4":
			upd()

		case "5":
			new()

		case "6":
			new_file()

		case "7":
			commands()

		case "8":
			os.system("clear")
			helper.help()

		case "10":
			ping_host.main()
			input(Fore.YELLOW + ("press enter to continue"))
			print("")
		case "11":
			more_apps()

		case "98":
			print(Fore.CYAN + '⭐⭐⭐⭐⭐')
			input("rate lin master out of 5 stars \n")
			print("Thank you for the 5 stars haha thankyou")
			print("Goodbye......")
			running = False

		case _:
			print(Fore.RED + f"error code 1: {choice} not an option")
