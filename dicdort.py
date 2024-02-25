import discord
from discord.ext import commands
#M7L2 get_class fonksiyonunu import ettik
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Saved the image to ./{attachment.filename}")
            # M7L2 de get_class fonksiyonun çağırdık
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt",
            image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")

bot.run("MTEzOTk0NjQ1MjAyMjQ4MDk5OA.GlCcPE.Pmh4Tm7D6g4D7QZFWlED0hmoLPSpeCEXLo-joM")
