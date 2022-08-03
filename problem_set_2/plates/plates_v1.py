def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")

def is_valid(s):
	if len(s) >= 2 and len(s) <= 6 and s.isalnum():
		if s[0:2].isalpha() and "0" not in s[2:5]:
			return True
	return False

main()
