import discord
import os
from discord.ext import commands
import string
from random import choice
from better_profanity import profanity

bot = commands.Bot(command_prefix='$')

character = string.ascii_letters + string.digits


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('The Techie'))
    print('main.py logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    randomizer = "".join(choice(character) for x in range(6)) + "-" + "".join(choice(character) for x in range(6))
    randomizer = randomizer + randomizer

    profanity.load_censor_words()

    # For Bad Words
    if message.author == bot.user:
        return

    if profanity.contains_profanity(message.content):
        await message.delete()
        censored_text = profanity.censor(message.content)
        await message.channel.send("Stop cussing you bum " + message.author.mention + "!")
        mod_channel = bot.get_channel(861396298888773703)
        await mod_channel.send(message.author.mention + " said " + censored_text)
        print(f'```{message.author.mention} + " said " + {censored_text}```')

    if message.author == bot.user:
        return

    if message.content.startswith('pass'):
        await message.channel.send("Please Check Your Dms " + message.author.mention)
        await message.author.send(f"```{randomizer}```")
    """
    count = 0
    x = [char for char in msg]

    for word in x:
        if word in words[0].split():
            count += 1
    
    if count == words[0]:
        await msg.channel.send(msg.author.mention + " said " + words[0])
"""

bot.run(os.getenv('TOKEN'))
