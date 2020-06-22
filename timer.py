import time
seconds = int(input("How many seconds to wait"))
for i in range(seconds):
	print(str(seconds - i) + "seconds remaining")
	time.sleep(1)#This is where all the magic happens
print("Time is up")