import discord
import os
from discord.ext import commands
import string
from random import choice

bot = commands.Bot(command_prefix='$')

character = string.ascii_letters + string.digits


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('The Techie'))
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    randomizer = "".join(choice(character) for x in range(16))

    if message.author == bot.user:
        return

    if message.content.startswith('gen'):
        await message.channel.send("Please Check Your Dms " + message.author.mention)
        await message.author.send(f"```{randomizer}```")


"""
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('fuck') or message.content.startswith('shit') or message.content.startswith(
            'bitch'):
        await message.delete()
        await message.channel.send(message.content)
"""


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked.')


bot.run(os.getenv('TOKEN'))
