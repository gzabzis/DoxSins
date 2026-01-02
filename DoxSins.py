# ----------------------------------------------------------------------------
# DoxSins - A tool created by gzabzis.
# 
# DISCLAIMER:
# - This script is for **educational purposes only**.
# - The creator (**gzabzis**) does not take responsibility for any **misuse** or **illegal activities** involving this tool.
# - The tool **must not be resold** or redistributed for profit.
# - By using this tool, you agree to take full responsibility for its use.
# ----------------------------------------------------------------------------

import os

# Red text color ANSI code
RED = '\033[31m'
RESET = '\033[0m'

# Updated ASCII Art Banner with much bigger "DoxSins"
banner = f"""
{RED} DDDD    OOO   X   X  SSSSS  III  N   N  SSSSS
 D   D  O   O   X X   S       I   NN  N  S
 D   D  O   O   X X   SSSSS   I   N N N  SSSSS
 D   D  O   O   X X       S   I   N  NN      S
 DDDD    OOO   X   X  SSSSS  III  N   N  SSSSS
{RESET}  

{{+}} Coded By gzabzis {{+}} ---------------
{{+}} GitHub.com/gzabzis/DoxSins.git {{+}} -------

Select an option from the menu below:

{{1}} - Information Gathering
{{2}} - Password Attacks
{{3}} - Wireless Testing
{{4}} - Exploitation Tools
{{5}} - Sniffing & Spoofing
{{6}} - Web Hacking
{{7}} - Private Web Hacking
{{8}} - Post Exploitation
{{9}} - INSTALL & UPDATE
{{10}} - CONTRIBUTORS
{{99}} - EXIT
"""

def menu():
    os.system("clear")  # Clear the terminal screen
    print(banner)

    # Wait for user input and interact
    while True:
        choice = input("Enter your choice (1-99): ")
        if choice == '1':
            print("Option 1: Information Gathering")
            # Add your functionality for option 1 here
        elif choice == '2':
            print("Option 2: Password Attacks")
            # Add your functionality for option 2 here
        elif choice == '99':
            print("Exiting the program...")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")

# Run the menu function
menu()
