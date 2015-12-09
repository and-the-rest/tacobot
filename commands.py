from random import randint

#######################
# Adding functions to tacobot
# - Name the function what you want the command to be to use it
# - Ex. 'def flipacoin' is called using $flipacoin
#
#######################

# Class containing commands and functions to do
class command:
	# List of commands
	def listCommands(self):
		return ("Check commandList.txt for available commands")

	#Example function
	def flipacoin(self):

		if (randint(0, 1) == 0):
			return ("Heads!")
		else:
			return ("Tails!")
