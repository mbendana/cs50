while True:
	fraction1, fraction2 = input("Enter a fraction (formatted as X/Y): ").split("/")
	if fraction1.isdigit() and fraction2.isdigit() and fraction1 <= fraction2 and fraction2 != "0":
		fraction1 = int(fraction1)
		fraction2 = int(fraction2)
		break
try:
	result = fraction1 / fraction2 * 100
except ZeroDivisionError:
	print("Can't didive by zero (0).")
else:
	if result <= 1:
		print("E")
	elif result >= 99:
		print("F")
	else:
		print(f"{result:.0f}%")
