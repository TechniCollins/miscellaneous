def userInput():
	Statements = []
	userStatements = str(input("Please type in all your statements and enter 67 when finished\n"))
	Statements.append(userStatements)

	while userStatements != "67":
		
		userStatements = str(input("Please type in all your statements and enter 67 when finished\n"))
		Statements.append(userStatements)
	print(Statements)
userInput()
"""negation = "it is not true that " + Statement1
conjunction = Statement1 + " " + Statement2
print(negation)"""
