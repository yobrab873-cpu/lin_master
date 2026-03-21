LIN_MASTER

Version: 1.0.0
Release Year: 2026
Author: Brian Njuguna Mwangi
License: MIT


🔹 What is LIN_MASTER?


LIN_MASTER is a modular Linux automation and pentesting framework designed for ethical hacking, system automation, and tool development.
It allows you to:
1. Automate common Linux tasks like updates, package installation, and file management.
2. Reuse modules and scripts
3. Run pentesting modules such as host scanning, port scanning, and social engineering simulations.
4. Develop and integrate your own tools within a safe, structured framework.
5. Combine existing tools like zphisher while keeping them organized, safe, and easy to use.
Think of LIN_MASTER as your all-in-one Linux companion for learning, experimentation, and automation in cybersecurity labs.

🔹 Instructions


Clone the repository into your /home directory:

1.cd /home

2.git clone https://github.com/yobrab873-cpu/lin_master.git


⚠️ Cloning outside /home may lead to path issues and module failures. LIN_MASTER assumes safe usage under /home.


3.Run the setup script to install dependencies and create a launcher:

1. cd /home/lin_master
2. bash setup.sh

   
If any dependency fails to install automatically, install it manually:
Python modules:

pip3 install colorama

System tools:

sudo apt install figlet git
After setup, you can launch LIN_MASTER from anywhere using:

lin
Use modules ethically
LIN_MASTER is intended for educational purposes and authorized testing only.
Do not target live systems or unauthorized networks.
Always stay within lab environments, simulations, or systems you own/are authorized to test.

🔹 First-Time Debug Checklist


If you encounter issues after cloning, follow these steps:
Check Python and pip installation:

python3 --version
pip3 --version


Ensure launcher exists in ~/bin and is executable:

ls -l ~/bin/lin

Test the launcher:

lin

Test modules individually:

python3 helper.py      # Help & banners
python3 ping_host.py   # Host scanning
python3 social.py      # Social engineering / phishing module
python3 linux.py       # Main menu
Verify .upd.sh exists if using the update function:
Bash
ls -la /home/LIN_MASTER/.upd.sh
Confirm all dependencies installed (Python + packages + figlet + git).


🔹 Structure Overview

LIN_MASTER/
├── main.py         # Main launcher
├── linux.py        # Core menu & module manager
├── helper.py       # Help & banners
├── colors.py       # Colorama wrapper for colored output
├── ping_host.py    # Fast host discovery module
├── social.py       # Social engineering / phishing module
├── setup.sh        # Automated setup & dependency installer
├── .upd.sh         # Optional system update script
└── zphisher/       # Optional phishing tool integration


🔹 Notes & Warnings


1.Always use LIN_MASTER ethically.
2.Avoid hardcoding paths for future tools — keep them module-independent.
3.Use lab environments or virtual machines for experimentation.
4.Regular backups are recommended when running any automation tasks.
