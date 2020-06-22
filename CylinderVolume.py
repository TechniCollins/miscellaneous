print("Enter radius and height;")
pie = 3.142
rad = float((input("Radius:\n")))
height = float(input("Length:\n"))
volume = pie *rad * rad * height
print(volume)

if volume <= 1200 and volume >0:
	print("It could be bigger")
elif volume >=9000:
	print("HUMANGOUS")
else:
	print("It could have been worse")

