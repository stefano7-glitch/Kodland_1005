import discord, os, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def inquinamento_definizione(ctx):
    await ctx.send(f"L’inquinamento è un’alterazione dell’ambiente, naturale o antropico, causata da elementi inquinanti. Questa alterazione può provocare disagi temporanei, patologie, danni permanenti alla vita umana, animale e vegetale. In senso più ampio, si tratta di una contaminazione di qualsiasi ambiente, spesso dovuta a rifiuti industriali, emissioni nocive o comportamenti umani non sostenibili.")

@bot.command()
async def inquinamento_immagini(ctx):
    img_name = random.choice(os.listdir('immagini inquinamento'))
    with open(f'immagini inquinamento/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def inquinamento_scelta(ctx):
    await ctx.send(f"Alcune persone non hanno rispetto per l'ambiente. Ma perché? Perche se ne fregano della natura pensando che non succederà niente, oppure lo sanno ma non glie ne frega niente. Abbiamo ancora una possibilità e dobbiamo sfruttarla al massimo, altrimenti sarà finita per noi.")

bot.run("MTM5MzUyODIzODAzODU4MTI1OQ.GP_OjN.4opmR3ojyRKevwal-Pwkivy-efq2IZTjte8sJs")
