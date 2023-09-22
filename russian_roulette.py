import random
import os
import sys

mag = [1, 0, 0, 0, 0, 0]

random.shuffle(mag)

begin = input("Would you like to play Russian Roullete?(y/n)")

def play_again():
	restart = input("Do you want to play again? [y/n]")
	if restart == "y":
		os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
	else:
		print("Coward")
		sys.exit(0)


count = 0

if begin == 'y':
	if mag[0] != 0:
		print("You're dead.")
		play_again()
	else:
		print("You got lucky.")
		play_again()

else:
	print("Coward.")





