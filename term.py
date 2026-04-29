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

print("gen2gang-terminal v1.1")
print("welcome to gen2gang-terminal. Set up your enviroment here")

name = input("Name > ")

passwd = getpass.getpass("password > ")

print("authentication: enter password")

while True:
    epass = getpass.getpass("> ")
    if epass == passwd:
        print("correct!")
        break
    else:
        print("Not quite right....")


print("Show information? Y/n")
ddone = input("> ").lower()
if ddone == "y":
    print(f"name:", name)
    print("(password hidden)")
    print("")
else:
    print("Not shown. See again with: info.user")
    print("")

print("Setup finished")
print("Use help for a list of commands")
print("")
print("Welcome to your new account!")


sh = f"{name}@gen2> "

while True:
    term = input(sh)

    if term == "help":
        print("help      - show this menu")
        print("info      - display system info")
        print("info.user - show user configuration during setup")
        print("clear     - clear the screen")
        print("exit      - exit terminal")
        print("echo      - print a message")
        print("trigger   - triggers a process. see trigger-help for more")

    elif term == "clear":
        clear_screen()

    elif term == "exit":
        print("bye")
        break

    
    # fastfetch config btw
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

    elif term == "echo":
        echo = input("> ")
        print(echo)

    elif term == "trigger":
        print("trigger is a command that runs certain processes.")
        print("for a list of runable processes see trigger-help")

    elif term == "trigger-help":
        print("Use commands like the shown example: trigger-proc (replace proc with a process from the list)")
        print("crash        - attempt to kill init")
        print("")

    elif term == "trigger-crash":
        print("Kernel panic - not syncing: Attempted to kill init!")
        time.sleep(0.5)
        print("CPU: 0 PID: 1 Comm: init Not tainted 5.10.0-gen2 #1")
        print("Hardware name: ",platform.machine())
        print("Call Trace:")
        print(" dump_stack+0x6d/0x8b")
        print(" panic+0x101/0x2e3")
        print(" do_exit+0x8a7/0xa00")
        print(" do_group_exit+0x3a/0xa0")
        print(" get_signal+0x2f3/0x8c0")
        print(" do_signal+0x36/0x6f0")
        print(" exit_to_user_mode_prepare+0x12a/0x1b0")
        print("---[ end Kernel panic - not syncing: Attempted to kill init! ]---")
        time.sleep(2)
        break

    else:
        print("not a valid command")
