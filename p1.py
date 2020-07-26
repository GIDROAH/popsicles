import os 
import sys

x = int(input("Popsicles = "))
y = int(input("Siblings = "))

#formula of division
z = x % y
print(z)

if z == 0:
	print("give away")
else:
	print("eat them yourself")
	
#restart session
os.execl(sys.executable, sys.executable, *sys.argv)
