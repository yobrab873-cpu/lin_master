import colors as c
import os
import time

# Clear screen at the very beginning
os.system("clear")

boot_messages = [
    "Welcome to LIN_MASTER - Your Linux Pentesting Toolkit",
    "Released: 2026",
    "Created by Brian Njuguna",
    "Loading modules for ethical hacking...",
    "Remember: Ethics first, skills second",
    "Tip: Always backup before scanning",
    "Did you know? Python powers most pentesting tools",
    "Fun fact: Kali Linux is based on Debian",
    "LIN_MASTER is your cybersecurity companion",
    "Remember: Stay disciplined, stay learning",
    "Pro tip: Use strong passwords for all tools",
    "This tool is for educational purposes only",
    "Keep your system updated for security",
    "Motivation: Practice makes perfect",
    "Next module loading... Prepare yourself",
    "LIN_MASTER: Built to empower aspiring hackers",
    "Hack the mind, not the system",
    "Stay humble, ignore negativity, focus on mastery",
    "Your journey to financial freedom starts with discipline"
]

# Print all boot messages with a short delay
for sent in boot_messages:
    print(c.cyan() + sent)
    time.sleep(0.8)  # Slightly faster for smoother boot

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
