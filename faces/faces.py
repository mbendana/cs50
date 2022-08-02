def main():
	print(convert(input()))

def convert(text):
	text = text.replace(":)", "🙂").replace(":(", "🙁")

	return text

main()
