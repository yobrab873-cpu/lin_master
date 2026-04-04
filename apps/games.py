#games




from colorama import Fore, Style, init
init(autoreset=True)
import random
def number_ninja():

	score = 0
	attempts = 0
	levels = [x for x in range(1, 101)]

	current_level = 0
	max = 0
	run = True
	while run:
		max += 10
		current_level += 1
		print("""
	1.Play
	2.Exit
""")
		pl_choice = input(": ")
		if pl_choice == "1":
			answer = random.randint(0, max)
			print(Fore.GREEN + '''
	RULES
=> The computer has choosen a number
=> The user is given 5 attempts for each round to guess the secret number
=> The user is given clues
''')
			if current_level >100:
				print(Fore.RED + "You finished the game")
				run = False

			print(Fore.CYAN + f"level {current_level}")
			print(f"Guess the secret number from 0 to {max}")
			while attempts != 5:
				user = int(input("enter your guess: "))
				if user == answer:
					print(Fore.GREEN + f"Correct ✓ : guessed the number in {attempts} attempts:")
					break

				elif user > answer:
					attempts += 1
					print(f"Too high {attempts} attempts remaining")
				elif user < answer:
					attempts += 1
					print(f"Too low {attempts} attempts remaining")
				else:
					print("Failed")

		elif pl_choice == "2":
			print(Fore.BLUE + "exiting.......")
			input("enter to continue")
			run = False

		else:
			max -= 10
			current_level -= 1
			print(Fore.RED + "invalid syntax")

