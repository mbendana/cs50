def main():
	userTime = input("Enter a time: ")

	if userTime.endswith("a.m.") or userTime.endswith("p.m."):
		if convert(userTime) >= 7.0 and convert(userTime) <= 8.0 and userTime.endswith("a.m."):
			print("breakfast time")
		elif (convert(userTime) >= 12.0 and convert(userTime) < 13.0 or convert(userTime) == 1.0) and userTime.endswith("p.m."):
			print("lunch time")
		elif convert(userTime) >= 6.0 and convert(userTime) <= 7.0 and userTime.endswith("p.m."):
			print("dinner time")
	else:	
		if convert(userTime) >= 7.0 and convert(userTime) <= 8.0:
			print("breakfast time")
		elif convert(userTime) >= 12.0 and convert(userTime) <= 13.0:
			print("lunch time")
		elif convert(userTime) >= 18.0 and convert(userTime) <= 19.0:
			print("dinner time")

def convert(time):
	hours, minutes = time.split(":")
	hours = float(hours)
	minutes = float(minutes.split(" ")[0]) / 60
	return hours + minutes

#if __init__ == "__main__":
main()
