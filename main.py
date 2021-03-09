import discord
import os
import requests
import json

client = discord.Client()

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
      await message.channel.send("Here are the commands we have so far \n \n"
        "#Hello - gives you a nice greeting!\n"
        "#Quote - quotes a random quotes API\n"
        "#xkcd (number) - brings the designated xkcd comic number\n"
        "\nStay Tuned for more commands to be added in the future!")

    if message.content.startswith('#Hello'):
        print("Greeting user...")
        await message.channel.send('Hola, como estas?')
    
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
          print("Index out of range")
          await message.channel.send("Thats not a valid number, try again nerd!")
        except:
          print("you fuckin lose kiddo")
          await message.channel.send("I think that number is too large; Try again!") 

    
client.run('ODE4NjUyNzU3MDQ4MTY0MzYz.YEbLyw.3RcZb3kjpelZyOrLVMG9BvRY9fg')