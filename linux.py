import ping_host
import helper
import os
import time
import subprocess
import social

def clear():
	os.system("clear")

clear()

#-----------------------done---------------------#

print("All dependencies installed successfully!")

clear()


from colorama import Fore, Style, init
init(autoreset=True)

init()

banner = subprocess.getoutput("figlet LIN_MASTER")
print(Fore.GREEN + Style.BRIGHT + banner)

print(Fore.CYAN + "--------------------------------------------------")
print(Fore.MAGENTA + Style.BRIGHT + "WELCOME TO LINUX HELPER")
print(Fore.CYAN + "----------------------------------------[v1.0.0]----")
print(Fore.CYAN + "Developed by [CYBERNEST™] (©2026)")
print("")

print(Fore.GREEN + "loading.....")
time.sleep(1)

#--------main loop--------------#
running = True


#----------------PORT SCANNING FUNCTION---------------#
def dev():
	print(Fore.MAGENTA + "while adavancing this tool make sure you have a backup file: \n \n Do you want to continue \n yes \n no")
	sur = input(": "). lower()
	if sur == "y" or sur == "yes":

		os.system("nano /home/Lin_master/linux.py")



def port_scanner():
	clear()
	banner = subprocess.getoutput("figlet LIN_PORT SCANNER")
	print(Fore.YELLOW + Style.BRIGHT + banner)
	input(Fore.YELLOW + "press enter to continue")
#---------WEB EXPLOITATION FUNCTION--------------------#
def web():
	clear()
	banner = subprocess.getoutput("figlet LIN_WEB EXPLOITER")
	print(Fore.YELLOW + Style.BRIGHT + banner)
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
			os.system(f"mkdir {dir_name}")
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

#-----------------------learn-----------------------------#
def commands():
	clear()
	banner = subprocess.getoutput("figlet LIN_COMMANDS")
	print(Fore.YELLOW + Style.BRIGHT + banner)
	input(Fore.GREEN + "press enter to continue: ")
	print("")


#-------------------MENU----------------------------#
while running:
	clear()
	banner = subprocess.getoutput("figlet LIN_MASTER")
	print(Fore.GREEN + Style.BRIGHT + banner)

	print(Fore.CYAN + "--------------------------------------------------")
	print(Fore.MAGENTA + Style.BRIGHT + "WELCOME TO LINUX HELPER")
	print(Fore.CYAN + "----------------------------------------[v1.0.0]--")
	print(Fore.CYAN + "Developed by [CYBERNEST™] (©2026)")
	print("")
	print(Fore.YELLOW + "----------------MENU------------------")
	print("")

	print(Fore.MAGENTA + """
	 0. Develop linux master
	 1. Port scanning
	 2. Web exploitation
	 3. Phishing
	 4. Update system
	 5. Install package
	 6. Create files and Directories
	 7. Learn commands
	 8. Help
	 9. Exit
	10. Host enumaration
	""")
	print(Fore.YELLOW + "-----------------------------------------")
	print("Choose from menu")
	choice = input(": ")
	match choice:
		case "0":
			clear()
			dev()
		case "9":
			clear()
			running = False

		case "1":
			port_scanner()

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

		case _:
			print(Fore.RED + f"error code 1: {choice} not an option")
