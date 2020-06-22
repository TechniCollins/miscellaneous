import csv

def numberGenerator():
	file = open("numberDatabase.txt", "w+")
	for i in range(0, 100):
		number = "07054991" + str(i).zfill(2)
		file.write("%s\r\n" %number)
	print("Successfully added 99 phone numbers to the database")
	file.close()
numberGenerator()





# for x in range(0, 100):
# 	number = "07054991" + str(x).zfill(2)
# 	csvData = [['Name', 'Phone number'], ['Ann', number]]
# with open('contacts.csv', 'w+') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(csvData)

# csvFile.close()
