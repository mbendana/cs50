while True:
	fraction1, fraction2 = input("Enter a fraction (formatted as X/Y): ").split("/")
	if not (fraction1 > fraction2):
		try:
			fraction1 = int(fraction1)
			fraction2 = int(fraction2)
		except TypeError:
			pass
		except ValueError:
			pass
		else:
			try:
				result = fraction1 / fraction2 * 100
			except ZeroDivisionError:
				pass
			else:
				break

if result <= 1:
	print("E")
elif result >= 99:
	print("F")
else:
	print(f"{result:.0f}%")
