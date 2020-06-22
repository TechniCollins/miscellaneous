"""Stores a list of the logical connectives within the copound statement given"""
connectives = []
"""Stores a list of primitive statements by identifying individual letters
in the compound statement provided"""
statements = []
"""Stores identified brackets"""
brackets = []
"""Stores a list of symbols or letters that could't be identified"""
errorList = []
"""Stores the number of unidentified symbols/errors"""
errors = 0

#ask user to enter the statement and convert it to string
userStatement = "(p^(q<r))](/(p<(r^sl)))"#str(input("Please enter the statement to be analyzed\n"))

#Break down the string given to individual characters and put them in the array
#This will help identify logical connectives and statements
for x in userStatement:
	if x == "^":
		connectiveType = "conjunction"
		connectives.append(connectiveType + " " + x)

	elif x == "]":
		connectiveType = "disjunction"
		connectives.append(connectiveType + " " + x)
	elif x == "<":
		connectiveType = "implication"
		connectives.append(connectiveType + " " + x)
	elif x == ">":
		connectiveType = "double implication"
		connectives.append(connectiveType + " " + x)
	elif x == "/":
		connectiveType = "negation"
		connectives.append(connectiveType + " " + x)
	elif x == "(" or x == ")":
		brackets.append(x)
	elif x == "p" or x == "q" or x == "r" or x == "s":
		statements.append(x)
	else:
		errorList.append(x)
		errors = errors + 1

print("Please correct the following errors")
for n in errorList:
	print(n + " is not recognized as any logical connective or statement")
	
print("The following LOGICAL CONNECTIVES were identified: ")
for n in connectives:
	print(n)
