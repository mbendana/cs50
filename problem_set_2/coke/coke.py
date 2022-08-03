amount_due = 50
original_amount = 50
amount_entered = 0

while True:

	print("Amount Due:", amount_due)
	user_input = int(input("Insert Coin: "))
	if user_input == 25 or user_input == 10 or user_input == 5:
		amount_entered += user_input
		amount_due -= user_input
	if amount_entered == original_amount or amount_entered > original_amount:
		print("Change Owed:", amount_entered - original_amount)
		break
