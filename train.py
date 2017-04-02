"""
Training file for Hopfield
"""
import os

"""
Function to get an input text file for training samples
"""
def getSamples():
	print('\nPlease enter the name of your training samples file: ')
	try:
		train = input(">>> ")
		if train.endswith('.txt') and os.path.getsize(train) > 0:
			return train
	except FileNotFoundError:
		print("Invalid filename, please try again")
		getSamples()
	except TypeError:
		print("Please enter a string with the name of the text file")
		getSamples()
