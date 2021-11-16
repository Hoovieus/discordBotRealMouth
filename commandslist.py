#list of commands available to the bot

def command(commandName, commandPrefix, commandDescription):
  name = commandName
  cmd = commandPrefix
  desc = commandDescription
  command = (name + " is called by " + cmd + " which " + desc)
  command = command + "\n"
  return(command)

def commandlist(a,b,c, listName):
  item = command(a,b,c)
  listName.append(item)
  #print("attribute " + a + " added!")
  
cmdList = []
commandlist("Help","#help","opens a list of available commands.", cmdList)
commandlist("Hello","#hello","greets the user.", cmdList)
commandlist("Quote","#quote", "grabs a random quote from an API.", cmdList)
commandlist("XKCD","#xkcd","pulls up a specified xkcd comic. Requires a number.", cmdList)

finalList = ""

cmdList_length = len(cmdList)

for x in range(cmdList_length):
  finalList += (cmdList[x])

#print(cmdList)



