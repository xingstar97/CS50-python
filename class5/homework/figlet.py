import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
if len(sys.argv)==1:
    input = input("Input: ")
    font = random.choice(figlet.getFonts())
    figlet.setFont(font = font)
    print(figlet.renderText(input))
elif len(sys.argv) ==3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
        input = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(input))
    else:
        sys.exit("Provide the font!")
else:
    sys.exit("Incorrect command line arguments!")
        