userInput = input("Enter the name of a variable in camelCase format: ")

for text in userInput:
	if text.isupper():
		text = "_" + text.lower()
	print(text, end="")
print()
