import discord
import random
import env
import time

DEFAULT_CHANNEL = 1288337522027401256

intents = discord.Intents.default()

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

    jeremyShouts = [f"I think Jeremy is cool", f"Listen to your professors!"]

    if 'Jeremy' in message.content:
      await message.channel.send(jeremyShouts[random.randInt(0, 1)])

    if 'together' in message.content:
      await message.channel.send("Philosophy is done best in community. -Jeremy Reid")
    if 'someone wants' in message.content:
      await message.channel.send("Philosophy is done best in community. -Jeremy Reid")
    if 'who wants' in message.content:
      await message.channel.send("Philosophy is done best in community. -Jeremy Reid")
    
    ########--------- REFERENCES ---------########
    # if '<' == message.content:
    #   await message.channel.send(shouts[random.randint(0, 2)])
    # if '<<' == message.content:
    #   await message.channel.send(shouts[random.randint(0, 2)])
    # if '<--' == message.content:
    #   await message.channel.send(shouts[random.randint(0, 2)])
    # if '<---' == message.content:
    #   await message.channel.send(shouts[random.randint(0, 2)])
    # if '...' == message.content:
    #     await message.channel.send(f"te falta algo {author}?")
    
    # if 'blingers' in msgFormat:
    #   await message.channel.send('BLINGERS PILINGERS ASSEMBLE:bangbang:')
    # if 'lil blinger' in msgFormat:
    #     await message.channel.send(greetings[random.randint(0,2)])
    # if 'hola' in msgFormat:
    #   await message.channel.send(greetings[random.randint(0,2)])
    # if 'ora' in msgFormat:
    #   currentTime = time.strftime("%H:%M:%S", time.localtime())
    #   await message.channel.send(f"son las {currentTime}")
    # if 'puto' in msgFormat:
    #   await message.channel.send(f"puto tu {author}")
    # if 'madre' in msgFormat:
    #   await message.channel.send(f"la tuya {author}")
    # if 'shit' in msgFormat:
    #   await message.channel.send(f"A que hora pasas por el pan {author}")

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

client.run(env.TOKEN)
