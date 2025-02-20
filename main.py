import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

TOKEN = 'MTE4MzY2OTUxMjY5NzAzMjc1NQ.GJIQWU.nFtxTuPZKh2P3VMqVoWNPSyvM5OHiAIbffw7fA'


# ////////// message ////////

@bot.event
async def on_message(message):
    mes = message.content
    if mes == 'hello':
        await message.channel.send("Hello It's me")

    elif mes == 'hi bot':
        await message.channel.send("Hi, " + str(message.author.name))
    
    await bot.process_commands(message)



# ////////// command_prefix //////////

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx. author.name}!")



# ////////// Slash Commands //////////

@bot.tree.command(name="hellobot", description="Replies with Hello")
async def hellocommand(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! It's me, BOT DISCORD")


# //////// Bot Online //////////

@bot.event
async def on_ready():
    print("Bot Online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")

server_on()

bot.run(TOKEN)