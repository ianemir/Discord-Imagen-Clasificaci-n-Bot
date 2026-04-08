import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! Soy un bot de clasificación de imágenes. Usa el comando !check seguido de una imagen para obtener la clasificación.')
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name= attachment.filename
            file_url = attachment.url        
            await attachment.save(f"{file_name}")
            await ctx.send(f"¡Gracias por subir la imagen! La URL de tu imagen es: {file_url}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"{file_name}"))
    else:
        await ctx.send("No recibí ninguna imagen. Por favor, intenta de nuevo.")
bot.run('')