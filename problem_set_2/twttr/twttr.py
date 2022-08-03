user_input = input("Enter some text: ")

for c in user_input:
	if c.lower() not in ["a", "e", "i", "o", "u"]:
		print(c, end="")

print()
