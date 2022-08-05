items = {}
while True:
	try:
		userInput = input()
		if userInput in items:
			items[userInput] += 1
		else:
			items[userInput] = 1
	except EOFError:
		break

for item in sorted(items):
	print(items[item], item.upper())
