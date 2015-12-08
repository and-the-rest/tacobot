import connection  	

#Basic configuration infomration
server = "irc.rizon.net" 
channel = "#gstech" #using this for test server
botnick = "tacobot" 
port = 6667


# Create instance of the irc bot
ircbot = connection.connect(server, channel, botnick, port)