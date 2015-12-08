import socket

# Class the connects to server and retrieves/sends
class connect:

    def __init__(self, server, channel, botnick, port):
		ircsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ircsocket.connect((server, 6667)) 
		ircsocket.send("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n")
		ircsocket.send("NICK "+ botnick +"\n") 
		ircsocket.send("JOIN "+ channel +"\n")

		while 1:
			ircmsg = ircsocket.recv(2048) 
			ircmsg = ircmsg.strip('\n\r') 
			print(ircmsg)

			#if ircmsg.find(":$flipcoin"):
				#flipacoin()