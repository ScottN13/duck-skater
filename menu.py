import os
import sys
from rich.console import Console
from configparser import ConfigParser

config = ConfigParser(comment_prefixes="#", delimiters="=")
config.read("config/main.ini")
console = Console()



class engine():

    def clear(): os.system('cls' if os.name == 'nt' else 'clear')

    class error(): # error class for easy access
        def ini(): sys.exit("# error: main.ini not found")
        def emptyFirm(): sys.exit("# error: selected target has no firmware partition")
        def noSignature(): sys.exit("# error: selected firmware has no signature patch")
        def dumpError(): sys.exit('# error: dumping failed')
        def readError(): sys.exit("# error: couldn't read firmware patches")
        def commandNotRecognized(): sys.exit("# error: command not recognized")


    class flasher(): # the main flasher

        def __init__(self):
            ...


        def flash():
            engine.clear()
            print("Loading flasher...")
            try: # fetch signature patch from firmware folder
                sigPatchVer = str(config["MAIN"]["sigPatchVer"])
                print(f"Current SignaturePatch version is {sigPatchVer} in 'config/main.ini'")
            except:
                engine.error.ini()

            # fetch firmware
            # menu
            console.print("------------[bright_yellow][bold]DUCK[/][/]-[bright_red][bold]SKATER[/][/]------------")
            console.print("------------[bold]Flasher[/]------------")
            print(f"""Please select target media:
                        {os.listdrives()}
                  """)
            targetMedia = console.input("Target (case sensitive):")


        def patch():
            engine.clear()
            print("Fetching patch folder ('duck-skater/patches')")
            patchesFolder = os.listdir("patches/")
            print(f"Files found: {patchesFolder}")
            print("separating useless files from patches")


        def dump(): ...
        def update(): ...

    class menu():
        def header():
            console.print("------------[bright_yellow][bold]DUCK[/][/]-[bright_red][bold]SKATER[/][/]------------")

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
           csinp = console.input("[bright_yellow][bold]Enter a number from the list, then press enter: ")
           if csinp == "1":
                engine.flasher.flash()
           elif csinp == "2":
                engine.flasher.patch()
           elif csinp == "3":
                engine.flasher.dump()
           elif csinp == "4": print("not yet")
           elif csinp == "5": print("not yet")
           else:
               engine.error.commandNotRecognized()



# run the script
engine.menu.mainMenu()