import socket

# Class the connects to server and retrieves/sends
class connection2:

	def __init__(self, server, channel, botnick, port):
		ircsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ircsocket.connect((server, port)) # Here we connect to the server using the port 6667
		ircsocket.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutoral covered on http://shellium.org/wiki.\n") # user authentication
		ircsocket.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot
		ircsocket.send("JOIN "+ channel +"\n")

		while 1:
			ircmsg = ircsocket.recv(2048) 
			ircmsg = ircmsg.strip('\n\r') 
			print(ircmsg) 

# Simple class containing different commands
class commands:
	

#Basic configuration infomration
server = "irc.rizon.net"
channel = "#gstech"
botnick = "tacobot"
port = 6667


# Create instance of irc bot
ircbot = connection2(server, channel, botnick, port)



