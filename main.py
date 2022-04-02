import discord
from bot_settings import BotSettings
from query_analyser import Analyser
from reply_handler import Reply

client = discord.Client()
botSettings = BotSettings('bot_settings.json')

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
        reply_object = Reply(arguments, botSettings.settings['APIUrl'])
        reply_arguments = reply_object.get_arguments()
        coub_identifier = reply_object.get_reply()

        # Upload the video file with the name of the coub identifier.
        await message.channel.send(file=discord.File(coub_identifier + '.mp4'))
        #await message.channel.send(file=discord.File("test.mp4"))

        # Yeet the reply back to the user.
        await message.channel.send(coub_identifier)

# Initialize the bot.
client.run(botSettings.settings['Token'])