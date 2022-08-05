import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 3:
	if sys.argv[1] in ["-f", "--font"]:
		user_font = sys.argv[2]
		if user_font in figlet.getFonts():
			figlet.setFont(font=user_font)
		else:
			sys.exit(f"Invalid usage.\nUsage: {sys.argv[0]} [-f | --font <font_name>]")
	else:
		sys.exit(f"Invalid usage.\nUsage: {sys.argv[0]} [-f | --font <font_name>]")
elif len(sys.argv) == 1:
	user_font = random.choice(figlet.getFonts())
	figlet.setFont(font=user_font)
else:
	sys.exit(f"Invalid usage.\nUsage: {sys.argv[0]} [-f | --font <font_name>]")

user_input = input("Input: ")
print(figlet.renderText(user_input))
