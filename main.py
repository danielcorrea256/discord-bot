from dotenv import load_dotenv
import discord
import os
import requests
import random

def generate_quote():
    try:
        data = requests.get('https://api.quotable.io/random?maxLength=50&tags=wisdom|famous-quotes').json()
        message = data['content'] + " - " + data['author'] 
    except:
        message = "Hello World"
    return message


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot ready, logged as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("hello")
    elif message.content.startswith("$quote please"):
        await message.channel.send(generate_quote())

client.run(os.environ.get("TOKEN"))