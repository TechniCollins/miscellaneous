import random


def MegaJackpot():
	MegaProbability = str(3*(3**(16)))
	print("The probability that you will win The Mega Jackpot is "+ MegaProbability)
MegaJackpot()



# def UserGames():
# 	games= int(input("How many games do you want to place bets on?\n"))
# 	probability = str(3*(3**(games-1)))
# 	print("The probability that you will win is "+ probability)
# UserGames()

print("*************************SPORTSPESA ODDS***********************************")
print("""KEY
		 1: HOME WIN 
		 2: DRAW
		 3: AWAY WIN""")

def OddGenerator():
	gamesPlayed = 1
	while gamesPlayed <18:
		myOdds=[]
		for odds in range(1, 18):
			generatedOdds = random.randint(1, 3)
			myOdds.insert(0, generatedOdds)
		myDict = {"Possibility "+ str(gamesPlayed).zfill(2): myOdds}
		print(myDict)	

		gamesPlayed +=1
OddGenerator()
