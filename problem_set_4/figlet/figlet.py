import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
exit_message = f"Invalid usage.\nUsage: {sys.argv[0]} [-f | --font <font_name>]"

if len(sys.argv) == 3:
	if sys.argv[1] in ["-f", "--font"]:
		user_font = sys.argv[2]
		if user_font in figlet.getFonts():
			figlet.setFont(font=user_font)
		else:
			sys.exit(exit_message)
	else:
		sys.exit(exit_message)
elif len(sys.argv) == 1:
	user_font = random.choice(figlet.getFonts())
	figlet.setFont(font=user_font)
else:
	sys.exit(exit_message)

user_input = input("Input: ")
print(figlet.renderText(user_input))
