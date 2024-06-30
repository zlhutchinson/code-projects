# Basic Discord bot that launches batch file from local machine.

import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello! If you would like to start the minecraft server type $run. If I don't respond in the future, contact Zachary.")

    if message.content.startswith('$run'):
        await message.channel.send('Running...')
        os.chdir(r'C:\Users\Zachary\Desktop\Minecraft Server')
        os.system('RunServer.bat')

# Insert token provided by Discord Application here
token = ""

client.run(token)
