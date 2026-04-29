# import
# import
import os
import time
import platform
import getpass

# config
OS = ""
sh = "# "

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


print(" use with root privilages IF possible ")
print("welcome to gen2 gang terminal. Set up your enviroment here")

name = input("Name > ")

# hidden password input
passwd = getpass.getpass("password > ")

print("authentication: enter password")

while True:
    epass = getpass.getpass("> ")
    if epass == passwd:
        print("done!")
        break
    else:
        print("Not quite right....")


print("Done! show information? Y/n")
ddone = input("> ").lower()
if ddone == "y":
    print(f"name:", name)
    print("(password hidden)")  # don't show it anymore
else:
    print("Not shown. See again with: info.user")


print("Welcome to your new account!")

# nicer prompt
sh = f"{name}@gen2> "

while True:
    term = input(sh)

    if term == "help":
        print("help      - show this menu")
        print("info      - display system info")
        print("info.user - show user configuration during setup")
        print("clear     - clear the screen")
        print("exit      - exit terminal")

    elif term == "clear":
        clear_screen()

    elif term == "exit":
        print("bye")
        break

    elif term == "info":
        print("                ___  \n"
        "  __ _ ___ _ _ |_  ) \n"
        " / _` / -_) ' \\ / /  \n"
        " \\__, \\___|_||_/___|\n"
        " |___/              \n")
        print(f"user: ", name)
        print("OS:", platform.system(), platform.release())
        print("Version:", platform.version())
        print("Machine:", platform.machine())
        print("Processor:", platform.processor())

    elif term == "info.user":
        print(f"name:", name)
        print("(password hidden)")