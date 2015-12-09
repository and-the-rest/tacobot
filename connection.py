import socket 
import commands
import inspect 

# Creates an instance of command class under commands.py
getCommand = commands.command()

# Stores all the commands
commandsList = []

# Retrieves all the methods from commands.py to make a list of callable commands
def retrieveCommandList():
    for x in inspect.getmembers(commands.command, inspect.ismethod):
    	commandsList.append(x[0])

retrieveCommandList()

# Class that connects to server and retrieves/sends
class connect:

    def __init__(self, server, channel, botnick, port):
		ircsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ircsocket.connect((server, 6667)) 
		ircsocket.send("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n")
		ircsocket.send("NICK "+ botnick +"\n") 
		ircsocket.send("JOIN "+ channel +"\n")

		# Loop that runs while the bot is active
		while 1:
			ircmsg = ircsocket.recv(2048) 
			ircmsg = ircmsg.strip('\n\r') 
			print(ircmsg)


			# Checks if message is in list of commands and calls it
			for x in commandsList:
				if (ircmsg.find("$" + x) != -1):
					ircsocket.send("PRIVMSG " + channel + " :" + getattr(getCommand, x)() + "\n")
					#print (getattr(getCommand, x))()