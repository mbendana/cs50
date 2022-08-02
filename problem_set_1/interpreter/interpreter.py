def main():
	userInput = input("Enter an arithmetic expression (e.g.: 1 + 1): ")

	n1, op, n2 = userInput.split(" ")
	n1 = int(n1)
	n2 = int(n2)

	match op:
		case "+":
			print(f"{add(n1, n2):.1f}")
		case "-":
			print(f"{sub(n1, n2):.1f}")
		case "*":
			print(f"{mul(n1, n2):.1f}")
		case "/":
			print(f"{div(n1, n2):.1f}")
		case _:
			print("Unknown operator")

def add(n1, n2):
	return float(n1 + n2)

def sub(n1, n2):
	return float(n1 - n2)

def mul(n1, n2):
	return float(n1 * n2)

def div(n1, n2):
	return float(n1 / n2)

main()

