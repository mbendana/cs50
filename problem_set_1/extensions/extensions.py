filename = input("Enter a filename: ")

if filename.lower().endswith(".gif"):
	print("image/gif")
elif filename.lower().endswith(".jpg"):
	print("image/jpg")
elif filename.lower().endswith(".jpeg"):
	print("image/jpeg")
elif filename.lower().endswith(".png"):
	print("image/png")
elif filename.lower().endswith(".pdf"):
	print("application/pdf")
elif filename.lower().endswith(".txt"):
	print("text/plain")
elif filename.lower().endswith(".zip"):
	print("application/zip")
else:
	print("application/octet-stream")
