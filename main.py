import discord
import os
import requests
import json
#import commandslist
from commandslist import finalList

client = discord.Client()

packwatch = ["rip","bozo","ripbozo","Rip","Bozo","Ripbozo","pack","Pack", "smokin", "Smokin"]
mommy = ["mommy", "mom", "Mommy", "Mom", "milkers", "Milkers", "Sigmund", "Freud", "sigmund", "freud"]
csgo = ["csgo", "Csgo", "cSgo", "csGo", "csgO", "cs:go", "CSGO", "CS:GO"]
airtime = ["airtime"]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    return(quote)

def get_comic(number):
    response = requests.get("http://xkcd.com/"+ number +"/info.0.json")
    json_data = json.loads(response.text)
    comic = json_data['img']
    return(comic)

def getComic():
    response = requests.get("http://xkcd.com/info.0.json")
    json_data = json.loads(response.text)
    comic = json_data['img']
    return(comic)

@client.event
async def on_ready():
    print('Bot is Ready!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('#help'):
      print("Giving a helping hand...")
      await message.channel.send("Here are the commands we have so far: \n \n" 
        + finalList +
        "\nStay Tuned for more commands to be added in the future!")

    if message.content.startswith('#hello'):
        print("Greeting user...")
        nombre = str(message.author)
        await message.channel.send('Hola, como estas @' + nombre + ' ?')
    
    if message.content.startswith('#quote'):
        print("Quoting...")
        quote = get_quote()
        await message.channel.send(quote)
    
    if message.content.startswith('#xkcd'):
        try:
          print("Finding XKCD content...")
          comicNumber = message.content.split("#xkcd ", 1)[1]
          comic = get_comic(comicNumber)
          await message.channel.send(comic)
        except IndexError:
          print("Index out of range. Defaulting")
          comic = getComic()
          await message.channel.send(comic)
        except:
          print("you fuckin lose kiddo")
          await message.channel.send("I think that number is too large; Try again!") 

    if message.content.startswith('#colorRole'): 
        inputted = message.content.split()
        colorint = int(inputted[2], 16)
        ConsoleMessage = "Color " + inputted[1] + " created using Bot Cmd"
        await message.guild.create_role(name=inputted[1],color=colorint,reason=ConsoleMessage)
        print("role created")
        
    #word detection

    if any(word in message.content for word in packwatch):
      await message.channel.send("We smokin that opp pack?")
      await message.channel.send("https://media1.tenor.com/images/9408fa98a65609c4d4c909d06cc7a9f8/tenor.gif?itemid=18880647")
      print("pack smoked")

    if any(word in message.content for word in mommy):
      #await message.channel.send("We smokin that opp pack?")
      await message.channel.send("https://media.discordapp.net/attachments/494339601306222592/861476139621285888/image0.gif")
      print("mommy protocol activated")
    
    if any(word in message.content for word in csgo):
      #await message.channel.send("We smokin that opp pack?")
      await message.channel.send("CS:GO to the polls.")
      print("CSGO TO THE POLLS")
    
    if any(word in message.content for word in airtime):
      #await message.channel.send("We smokin that opp pack?")
      await message.channel.send("airtime\n")
      await message.channel.send("https://tenor.com/view/nick-young-nba-godlike-miss-basketball-gif-5267820")
      print("airtime")

client.run('ODE4NjUyNzU3MDQ4MTY0MzYz.YEbLyw.3RcZb3kjpelZyOrLVMG9BvRY9fg')