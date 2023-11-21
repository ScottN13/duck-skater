import os
import sys
from rich.console import Console

console = Console()


class engine():
    class flasher():
        def flash(): ...
        def patch(): ...
        def dump(): ...
        def update(): ...

    class menu():
        def header():
            console.print("------------[bright_yellow][bold]DUCK[/][/]-[bright_red][bold]SKATER[/][/]-----------")

        def logo():...
        
        def activeTask(job): print("## Task: "+job)
        def mainMenu():
           engine.menu.header()
           print("""Welcome to duck-skater!
                 
                 [1] - Flash
                 [2] - Patch
                 [3] - Dump
                 [4] - Extras
                 [5] - Credits and Changelog
                  
                 """)
           engine.menu.header()
           csinp = console.input("\n [bright_yellow][bold]Enter a number from the list, then press enter: ")
           return csinp

    
    mMenu = menu.mainMenu()
    if mMenu == 1:
        flasher.flash()
    elif mMenu == 2:
        flasher.patch()
    elif mMenu == 3:
        flasher.dump()
    elif mMenu == 4: print("not yet")
    elif mMenu == 5: print("not yet")



# run the script
engine.menu.mainMenu()