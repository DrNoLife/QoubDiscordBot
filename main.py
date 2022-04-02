import discord
from bot_settings import BotSettings
from query_analyser import Analyser
from reply_handler import Reply

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

        # Find possible arguments.
        arguments = Analyser(message.content).find_arguments()

        # Based on arguments find out how to reply to user.
        reply_object = Reply(arguments)
        reply_arguments = reply_object.get_arguments()
        reply_message = reply_object.get_reply()

        # Yeet the reply back to the user.
        await message.channel.send(reply_message)

# Load the bot settings and initialize the bot.
botSettings = BotSettings('bot_settings.json')
client.run(botSettings.settings['Token'])