availableTeamIds=[1, 2, 4, 5]
teamId = 0
teamIdGenerator = availableTeamIds[-1]

print(teamIdGenerator)

teamsInfo = {str(teamId).zfill(2):"Machester"}


print("****LIST OF TEAMS AVAILABLE IN THE DATABASE****")
for x in teamsInfo:
	print(teamsInfo)

def updateTeamList():
	global teamId
	newTeam = ''
	while newTeam != 'done':
		teamId +=1
		newTeam = input("Enter new team name")
		teamsInfo.update({teamId:newTeam})
	for x in teamsInfo:
		print (x)


def userPrompt():
	addPrompt = input("Do you wish to add more teams? y/n\n").lower()
	if addPrompt == "y":
		updateTeamList()
	elif addPrompt == "n":
		exit()
	else:
		print("Invalid choice")
		userPrompt()
userPrompt()

print(teamsInfo)
