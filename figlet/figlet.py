import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()
types = figlet.getFonts()

if len(sys.argv) == 1:
    ip = input("Input: ")
    figlet.setFont(font=choice(types))
    print(figlet.renderText(ip))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in types:
            ip = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(ip))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")


