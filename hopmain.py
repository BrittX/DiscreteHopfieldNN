"""
Main which calls the supporting functions/methods for Hopfield
"""

import hopmenu as hm

def main():
	# Greet user
	hm.greet()

	# Make menu repeat until user exits
	while(1):
		hm.menu()
		try:
			# Store input
			choice = int(input(">>> "))
			hm.pick_one(choice)
		except ValueError:
			print('Need to choose a number option from the menu')
			hm.pick_one(3) # Just exit the program
		except TypeError:
			print("The value needs to be an integer")
			hm.pick_one(3)

# Testing code
if __name__ == '__main__':
	main()