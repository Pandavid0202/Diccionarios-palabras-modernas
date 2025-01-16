import random
import discord
import os
from bot_logic import get_duck_image_url
from bot_logic import gen_pass
from discord.ext import commands


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hola")
    
@bot.command()
async def bye(ctx):
    await ctx.send("adios")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def repeat(ctx, times: int, content='WAA'):
    for i in range(times):
        await ctx.send(content)
        
@bot.command()
async def mem_rand(ctx):
    
    meme = os.listdir("image")
    meme_random = random.choice(meme)
    with open(f'image/{meme_random}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    
@bot.command()
async def gym_mem(ctx):
    
    meme = os.listdir("memes")
    meme_gym = random.choice(meme)
    with open(f"memes/{meme_gym}","rb") as f:
        
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("")
