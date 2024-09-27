import discord
import random
import os
import time

DEFAULT_CHANNEL = 1288337522027401256
# Get the TOKEN from the environment variable
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN environment variable is not set.")
print(f'-->>>>>>>>>>>>>Got Discord TOKEN={TOKEN}<<<<<<<<<<<<<--')

intents = discord.Intents.all()

client = discord.Client(intents=intents)

greetings = ["Hi!", "suuup", "buenas"]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return # Avoid the bot responding to itself
    
    author = message.author.mention
    msgFormat = message.content.lower()
    allowed_mentions = discord.AllowedMentions(everyone = True)

    print(f'Got a new message=\'{message.content}\'\n\tguild={message.guild}\n\tauthor={message.author.name}')

    jeremyShouts = [f"I think Jeremy is cool", f"Listen to your professors!"]
    phillGreetings = [f'Hi, {author}!', f'How\'s it going?']

    # The message to be sent out to the message.channel
    messageToSend = ""

    if 'Hi Phill' in msgFormat:
      messageToSend = phillGreetings[1]
    if 'Jeremy' in msgFormat:
      messageToSend = jeremyShouts[random.randint(0, 1)]

    if 'together' in message.content:
      messageToSend = f'Philosophy is done best in community.\n\t\t-Jeremy Reid'
    if 'someone wants' in msgFormat:
      messageToSend = f'Philosophy is done best in community.\n\t\t-Jeremy Reid'
    if 'who wants' in msgFormat:
      messageToSend = f'Philosophy is done best in community.\n\t\t-Jeremy Reid'

    # Only send messageToSend if the string is not empty
    if messageToSend:
      print(f"Sending message: {messageToSend}")
      await message.channel.send(messageToSend)

# @client.event
# async def on_message_delete(message):
#     await message.channel.send(f"{message.author.mention}, why would you delete that message?")
    
@client.event
async def on_member_join(member):
    println(f"{member} joined")
    channel = client.get_channel(DEFAULT_CHANNEL)
    if not channel:
        return
    await channel.send(f"Welcome to PHIL 715, {member}!")

client.run(TOKEN)
