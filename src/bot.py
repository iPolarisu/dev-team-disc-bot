import discord
from discord.ext import commands, tasks
import datetime
import os
import json

DISCORD_TOKEN =

intents=discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')

@bot.command()
async def crearrol(ctx, nombre_rol):

    guild = ctx.guild
    try:
        nuevo_rol = await guild.create_role(name=nombre_rol)
            
        await ctx.send(f'Se ha creado el rol {nuevo_rol.mention}.')
    except discord.Forbidden:
        await ctx.send("No tengo permisos para crear roles.")

@bot.command()
async def test(ctx):
    canal_id = 
    canal = bot.get_channel(canal_id)
    equipo = "ComputerVision"
            
    if canal:
        # Obtén el rol del equipo por nombre (asegúrate de que el nombre coincida exactamente)
        rol_equipo = discord.utils.get(canal.guild.roles, name=equipo)
        if rol_equipo:
            # Verifica si el bot está en el "vecindario" del canal
            if bot.user in canal.members:
                # Menciona el rol en el mensaje
                mensaje = f'Recordatorio para el equipo {rol_equipo.mention}: ¡Es hora de la reunión!'
                await canal.send(mensaje)

bot.run(DISCORD_TOKEN)
