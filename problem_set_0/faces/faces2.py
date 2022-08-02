def main():
	print(convert(input()))

def convert(text):
	if ":)" in text:
		text = text.replace(":)", "🙂")
	if ":(" in text:
		text = text.replace(":(", "🙁")

	return text

main()
