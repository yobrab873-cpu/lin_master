import colors as c
import os
import time

# Clear screen at the very beginning
os.system("clear")

boot_messages = [
    "||                                        ]",
    "[|||||||||                                ]",
    "[||||||||||||                             ]",
    "[||||||||||||||||                         ]",
    "[||||||||||||||||||||||                   ]",
    "[||||||||||||||||||||||||||               ]",
    "[|||||||||||||||||||||||||||||            ]",
    "[||||||||||||||||||||||||||||||||         ]",
    "[||||||||||||||||||||||||||||||||||||     ]",
    "[|||||||||||||||||||||||||||||||||||||||  ]",
    "[|||||||||||||||||||||||||||||||||||||||||]"
]

# Print all boot messages with a short delay
for sent in boot_messages:
    print(c.cyan() + sent)
    time.sleep(0.3)  # Slightly faster for smoother boot

# After boot messages, display the menu
print("\n" + c.green() + "===============================================================")
print(c.cyan() + "                       LIN_MASTER BOOTED                   ")
print(c.green() + "==============================================================")
print("")
print(c.yellow() + "1. Menu ✓")
print(c.yellow() + "2. Exit x")

opt = input(c.green() + "|====| \n")

if opt == "1":
    import linux
else:
    exit()
