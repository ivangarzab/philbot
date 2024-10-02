import os
import random
import discord
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime, timedelta

DEFAULT_CHANNEL = 1288337522027401256
# Get the TOKEN from the environment variable
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN environment variable is not set.")
print(f'~~~~~~Got Discord TOKEN={TOKEN}~~~~~~')

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'~~~~~~We have logged in as {client.user}~~~~~~')

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

    if 'phill' in msgFormat:
      messageToSend = random.choice(phillGreetings)
    if client.user in message.mentions:
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

    # This line is necessary to process commands within on_message()
    await client.process_commands(message) 
    
@client.event
async def on_member_join(member):
    println(f"{member} joined")
    channel = client.get_channel(DEFAULT_CHANNEL)
    if not channel:
        return
    await channel.send(f"Welcome to PHIL 715, {member}!")

############################# REMINDER MESSAGES #############################
# Define the async task that will send messages for 
@tasks.loop(weeks=1)  # Runs every week 
async def send_reminder_message():
  now = datetime.utcnow()
  # Check if it's Tuesday for the wishing good luck in class
  if now.weekday() == calendar.TUESDAY:
    if now.hour == 15: # Check if current hour matches target hour
      channel = client.get_channel(DEFAULT_CHANNEL)
      if channel:
        await channel.send("Have fun in class!")
  # Check if it's Monday for the homework reminder
  elif now.weekday() == calendar.MONDAY:
    if now.hour == 20: # Check if current hour matches target hour
      channel = client.get_channel(DEFAULT_CHANNEL)
      if channel:
        await channel.send("Don't forget to submit in your homework tonight!")
  else:
    print(f"Ran send_reminder_message() at {now}, but there's nothing to shout.")

############################# CUSTOM COMMANDS #############################
@client.command()
async def rolldice(ctx: commands.Context):
    print(f"Got a rolldice command")
    result = random.randint(1, 6)
    await ctx.send(f"You rolled a {result}!")

@client.command()
async def flipcoin(ctx: commands.Context):
    print(f"Got a flipcoin command")
    result = random.choice(["HEADS", "TAILS"])
    await ctx.send(f"You flipped a coin and got {result}!")

################################ EXEC INIT ################################
# Start the task before the bot is ready
async def before_loop():
  await client.wait_until_ready()

send_reminder_message.start(before_loop)

# Run the bot with your bot token
client.run(TOKEN)
