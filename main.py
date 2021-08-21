import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType


client = commands.Bot(command_prefix='a!', intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.do_not_disturb,
        activity=discord.Game(f"On {len(client.guilds)} servers | a!help"))
    print('online!')
    DiscordComponents(client)


@client.command()
async def ping(ctx):
    embed = discord.Embed(
        description=
        f"** 🏓 Pong ! The Latency is ** **`{round(client.latency * 1000)}`** ms ",
        color=0x05a5e5)
    await ctx.send(embed=embed) 

client.run(' [ Paste Your Bot Token Here ] ')
