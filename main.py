import discord
from discord.ext import commands
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

# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)

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

    phillGreetings = [f'Hi, {author}!', f'How\'s it going?', '👋']
    jeremyShouts = [f"I think Jeremy is cool", f"Listen to your professors!"]

    # The message to be sent out to the message.channel
    messageToSend = ""

    if 'hi phill' in msgFormat:
      messageToSend = random.choice(phillGreetings)
    if 'hey phill' in msgFormat:
      messageToSend = random.choice(phillGreetings)
    if 'phill' in msgFormat:
      messageToSend = random.choice(phillGreetings)

    # Jeremy responses, and his quotes
    if 'jeremy' in msgFormat:
      messageToSend = random.choice(jeremyShouts)
    ### Philosophy is done best in community
    if 'together' in message.content:
      messageToSend = f'Philosophy is done best in community.\n\t\t-Jeremy Reid'
    if 'someone wants' in msgFormat:
      messageToSend = f'Philosophy is done best in community.\n\t\t-Jeremy Reid'
    if 'who wants' in msgFormat:
      messageToSend = f'Philosophy is done best in community.\n\t\t-Jeremy Reid'
    if 'share' in msgFormat:
      messageToSend = f'Philosophy is done best in community.\n\t\t-Jeremy Reid'
    
    # Papers
    if 'final paper' in msgFormat:
      messageToSend = f'Good papers grow themselves.'
    if 'papers' in msgFormat:
      messageToSend = f'Good papers grow themselves.'

    # Socrates
    if 'examine' in msgFormat:
      messageToSend = f'The unexamined life is not worth living.\n\t\tSocrates'
    if 'know' in msgFormat:
      messageToSend = f'All I know is that I know nothing.\n\t\tSocrates'
    # Descartes
    if 'i think' in msgFormat:
      messageToSend = f'I think, therefore I am.\n\t\Descartes'

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

@client.command()
async def rolldice(ctx: commands.Context):
    print(f"Got a rolldice command")
    result = random.randint(1, 6)
    await ctx.send(f"You rolled a {result}!")

@client.command()
async def flipcoin(ctx: commands.Context):
    print(f"Got a flipcoin command")
    result = random.choice(["Heads", "Tails"])
    await ctx.send(f"You flipped a coin and got {result}!")

client.run(TOKEN)
