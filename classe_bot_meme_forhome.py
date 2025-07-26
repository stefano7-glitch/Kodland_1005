import discord, os, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def inside_out_meme(ctx):
    img_name = random.choice(os.listdir('inside out meme images'))
    with open(f'inside out meme images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)
