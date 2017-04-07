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
		# Try to open the file and store its contents
		with open(train) as training:
			contents = training.readlines()
		hopAlgo(contents)
		return contents
	except FileNotFoundError:
		print("Invalid filename, please try again")
		getSamples()

"""
Function to read and store each line in training file
"""
def hopAlgo(tContents):
	# Store contents as # inputs, training pairs
	#tpairs = ""
	tpairs = []
	for i, item in enumerate(tContents):
		if i == 0: ins = int(item)
		elif i == 1: pairs = int(item)
		# Not include initial new line before training pairs
		elif i == 2 and item == '\n': continue
		else:
			tpairs.append(item)
		
	"""
	Probs put in its own function, but this stores each training pair
		as it's own list within the trains list
	"""
	i = 0
	trains = [[] for x in range(pairs)]
	for tset in trains:
		for item in tpairs[i:]:
			if item == '\n': 
				i+=1 # increment the index at end of training pair
				break
			tset.append(item)
			i+=1

	print("this is trains", trains)