import discord
from bot_settings import BotSettings

client = discord.Client()

# Event for whenever the bot is ready.
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')


# Event for whenever a message is received.
@client.event
async def on_message(message):
    # If the message is from the bot, ignore it.
    if message.author == client.user:
        return

    # If the message is "!qoub", find possible arguments and make the proper reply.
    if message.content.startswith('!qoub'):
        await message.channel.send('I am not fully functional yet. But later on, I\'ll reply to your message with a Coub.')

# Load the bot settings and initialize the bot.
botSettings = BotSettings('bot_settings.json')
client.run(botSettings.settings['Token'])