import connection

# Simple class containing different commands
#class commands:
    	

#Basic configuration infomration
server = "irc.rizon.net" 
channel = "#gstech" 
botnick = "tacobot" 
port = 6667


# Create instance of irc bot
ircbot = connection.connect(server, channel, botnick, port)



