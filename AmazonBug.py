def suffixGenerator():
	suffix = ""
	username = input("Enter username: ").capitalize()
	endUsername = username[-1]
	if endUsername == "s":
		suffix = "'"
	else:
		suffix = "'s"
	userSuffix = username + suffix + " Amazon account"
	print(userSuffix)
suffixGenerator()