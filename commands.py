from random import randint

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