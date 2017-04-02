"""
Menu portion for Hopfield NN
"""
import sys
import os
import train as t

def menu():
	print("\n Please choose one of the options below")

	print("1. Train using a training image file")
	print("2. Test using trained weight file")
	print("3. Exit \n")

"""
Print initial greeting
"""
def greet():
    print('Welcome to my Discrete Hopfield Neural Network!\n')


"""
Function that calls the selected method to run.

Arg:
    choice - integer value for menu option
"""
def pick_one(choice):
    try: 
        if choice in menu_choice:
            val = menu_choice[choice]()
    # User entered number that's not valid
    except ValueError:
        print("Error: Invalid selection")
        time.sleep(1)
        menu()
    except KeyboardInterrupt: 
        os.system('clear')
        menu_choice[3]()

# Options for menu
menu_choice = {"menu": menu,
        # 1: imageTrain, # Call from train.py
        1: t.getSamples,
        # 2: imageTest, # Call from test.py
	    3: sys.exit,
        }
