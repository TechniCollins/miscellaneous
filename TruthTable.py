"""TRUTH TABLE PROGRAM
   Version: TT1 (Truth Table 1)
   License: Free & Open source
"""

"""THE ACTUAL CONNECTIVES
¬

"""
def identifier():
	"""Stores a list of the logical connectives within the compound statement given"""
	connectives = []
	"""Stores primitive statements by identifying individual letters 
	in the compound statement provided."""
	statements = []
	"""Stores identified brackets"""
	brackets = []
	"""Stores a list of symbols or letters that could't be identified"""
	errorList = []
	"""Stores the number of unidentified symbols/errors"""
	errors = 0
	#Stores the number of statements identified
	statementNumbers = 0
	#Stores a calcuated number of possiblities of Truth status
	possiblities = 0
	#ask user to enter the statement and convert it to string
	userStatement = "(p^(q<r))](/(p<(r^s)))"#str(input("""Please enter the statement to be analyzed\nUse the letters p, q, r, s for stetements))
	#Break down the string given to individual characters and put them in the array
	#This will help identify logical connectives and statements
	for x in userStatement:
		if x == "^":
			"""connectiveType is a list with 2 indices
			that stores the name of the connective and how it's read in English"""
			connectiveType = ["conjunction", "And"]
			connectives.append(connectiveType[0] + " " + x + " read in enlish as " + "'" + connectiveType[1] + "'" )

		elif x == "]":
			connectiveType = ["disjunction", "Or"]
			connectives.append(connectiveType[0] + " " + x + " read in enlish as " + "'" + connectiveType[1] + "'" )
		elif x == "<":
			connectiveType = ["implication", " if...else"]
			connectives.append(connectiveType[0] + " " + x + " read in enlish as " + "'" + connectiveType[1] + "'" )
		elif x == ">":
			connectiveType = ["double implication", " if and only if"]
			connectives.append(connectiveType[0] + " " + x + "read in enlish as " + "'" + connectiveType[1] + "'" )
		elif x == "/":
			connectiveType = ["negation", " Not"]
			connectives.append(connectiveType[0] + " " + x + "read in enlish as " + "'" + connectiveType[1] + "'" )
		elif x == "(" or x == ")":
			brackets.append(x)
		#This section of the code identifies statements, uses
		#the count method to identify how many times they appear, 
		#then uses the information to update the statementNumbers 
		#variable. These will be useful in calculating accurate number 
		#of possibilities and avoiding counting of a statement more than once
		elif x == "p":
			pnumbers = (statements.count("p"))
			if pnumbers < 1:
				statementNumbers +=1
				statements.append(x)
		elif x == "q":
			qnumbers = (statements.count("q"))
			if qnumbers < 1:
				statementNumbers +=1
				statements.append(x)
		elif x == "r":
			rnumbers = (statements.count("r"))
			if rnumbers < 1:
				statementNumbers +=1
				statements.append(x)
		elif x == "s":
			snumbers = (statements.count("s"))
			if snumbers < 1:
				statementNumbers +=1
				statements.append(x)
		#END OF THE SECTION	
			
		else:#Any other unidentified characters are considered errors
			errorList.append(x)
			errors += 1
	if errors > 0:
		print("Please correct the following errors")
		for n in errorList:
			print(n + " is not recognized as any logical connective or statement")
	else:
		print("The following LOGICAL CONNECTIVES were identified: ")
		for n in connectives:
			print(n)
		print("\nThe following STATEMENTS were identified: ")
		for x in statements:
			print(x)
			#print(repr(x).rjust(2), repr(x.rjust(3)), repr(x).rjust(4))
		#calculate the number of possiblities (Ts and/or Fs)
		possiblities = 2**statementNumbers
		print("number of possibilities is " + str(possiblities))

	"""Using recursion to propmpt for a valid statement
	 as long as there are errors in the one provided"""
	while errors > 0:
		#print(str(errors) + " ERRORS identified:")
		identifier()
identifier()