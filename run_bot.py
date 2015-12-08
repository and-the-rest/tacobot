import socket

# Class the connects to server and retrieves/sends
class connection2:
	
    def __init__(self, server, channel, botnick, port):
		ircsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ircsocket.connect((server, port))
		ircsocket.send("USER "+ botnick +" "+ botnick +" "+ botnick + botnick)
		ircsocket.send("NICK "+ botnick +"\n") 
		ircsocket.send("JOIN "+ channel +"\n")

		while 1:
			ircmsg = ircsocket.recv(2048)
			ircmsg = ircmsg.strip('\n\r')
			print(ircmsg)

			if ircmsg.find("$taco") != -1: # if the server pings us then we've got to respond!
				print "taco"


# Simple class containing different commands
#class commands:
    	

#Basic configuration infomration
server = "irc.rizon.net"
channel = "#gstech"
botnick = "tacobot"
port = 6667


# Create instance of irc bot
ircbot = connection2(server, channel, botnick, port)



