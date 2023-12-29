# bot.py
import discord
from discord.ext import commands
import responses  # Este es el módulo que manejará las respuestas del bot

# Inicializar bot
intents = discord.Intents.default()
intents.messages = True  # Habilita el intent para leer mensajes
intents.message_content = True # Habilita el intent

bot = commands.Bot(command_prefix="/", intents=intents, help_command= None)

# Evento que se ejecuta cuando el bot se ha conectado y está listo
@bot.event
async def on_ready():   
    print(f'Bot conectado como {bot.user.name}')

# Comando de recomendación
@bot.command(name='recomendar', help='Recomienda una canción basada en el título y artista dados')
async def recomendar(ctx, titulo, artista: str):
    intro_message = ("!Saludos Humano! 😊 Soy Harmonize y poseo una base de datos de más de 600k canciones "
                     "de los años 60's, 70's y 80's. Aquí hay unas recomendaciones "
                     "basadas en tu canción solicitada:")
    await ctx.send(intro_message)
    # Llamar a la función de recomendación y obtener la respuesta
    response = responses.get_recommendation(titulo, artista)
    for link in response:
    # Enviar la respuesta al canal de Discord
        if link.startswith("https://www.youtube.com/watch?v="):
            await ctx.send(link)

@bot.command(name='helpharmonize')
async def help_command(ctx):
    help_text = "Aquí están los comandos que puedes usar:\n"
    help_text += "/recomendar <título> <artista> - Recomienda una canción basada en el título y artista dados\n"
    help_text += "Intenta no cometer errores en la definicion de tu petición"
    await ctx.send(help_text)

# Ejecutar el bot
bot.run('MTE4MDk0NzU5OTAyNTUyMDc2Mg.GKn81u.tMUwZpNIMAOwImzpZrxT-zB-v9vGX_4hxXDk20')

