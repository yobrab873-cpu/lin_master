import colors as c
import os
import time

# Clear screen at the very beginning
os.system("clear")




load = "|"

t = 0
for x in range(60):
	t += 1
	print("[" + "|" * t + "]", end="\r")
	time.sleep(0.03)

# Print all boot messages with a short delay
# After boot messages, display the menu
print("\n" + c.green() + "===============================================================")
print(c.cyan() + "                       LIN_MASTER BOOTED                   ")
print(c.green() + "==============================================================")
print("")
print(c.yellow() + "1. Menu ✓")
print(c.yellow() + "2. Exit x")

opt = input(c.green() + "|====| \n  ")

if opt == "1":
    import linux
else:
    exit()
