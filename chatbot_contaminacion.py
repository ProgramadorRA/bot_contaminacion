


import random

import discord


from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

respuestas = ["Apaga las luces cuando no las necesites","Cierra la llave mientras te cepillas los dientes.","Separa la basura para reciclar.","Usa menos plástico.","Ahorra agua al bañarte."]

bot_contaminacion = commands.Bot(command_prefix='-', intents=intents)

@bot_contaminacion.event
async def on_ready():
    print("bot en linea ve a dicord")
@bot_contaminacion.command()
async def hola(ctx):
    await ctx.send("hola como estas¿Quieres que te ayude a cuidar el medio ambiente?")
@bot_contaminacion.command()

async def si(ctx):
    await ctx.send(random.choice(respuestas))





