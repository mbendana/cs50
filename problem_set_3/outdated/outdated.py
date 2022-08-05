months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

while True:
	user_date = input("Date: ")
	if "/" in user_date or "," in user_date:
		if "/" in user_date:
			month, day, year = user_date.split("/")
		elif "," in user_date:
			month, day, year = user_date.split(" ")
			month = months.index(month) + 1
			day = day.strip(",")
	break

print(f"{year}-{month}-{day}")
