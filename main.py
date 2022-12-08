from dotenv import load_dotenv
import discord
import os
import requests

def generate_latex(eq):
    url = "https://latex.codecogs.com/png.image?\dpi{150}\\bg{white}"
    url += eq.replace(" ", "").replace("+", "&plus;").replace("\b", "\\b")
    return url

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
    elif message.content.startswith("$$") and message.content.endswith("$$"):
        await message.channel.send(generate_latex(message.content[2:-2]))

client.run(os.environ.get("TOKEN"))