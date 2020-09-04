altitude =int(input("Enter Plane Landing Altitude : "))

if(altitude <= 1000):
	print("Safe to Land")

if(altitude>1000 and altitude<=5000):
	print("Bring down to 1000")

if(altitude > 5000):
	print("Turn Around")