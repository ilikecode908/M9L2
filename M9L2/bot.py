import requests
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

city = "Ankara"

@bot.command()
async def start(ctx):
    await ctx.send("Merhaba, ben have durumu tahmini sesli okuyan bir botum")


@bot.command()
async def hava(ctx):
    url = f"https:wttr.in/{city}?format=3"
    response = requests.get(url)
    await ctx.send(response.text)


bot.run("")
