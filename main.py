import datetime
import os

import discord
import requests_cache
from discord.ext import commands
from dotenv import load_dotenv

from heroes import get_bad_against
from insults import InsultGenerator

load_dotenv()
help_command = commands.DefaultHelpCommand()

bot = commands.Bot(
    command_prefix="dc/",
    help_command=help_command,
    description="Some basic Dota 2 utilities",
    case_insensitive=True
)
game = discord.Activity(
    name="DOTA 2",
    type=discord.ActivityType.playing,
    start=datetime.datetime.utcnow()
)

requests_cache.install_cache('cache')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=game)
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def whois(ctx, *, keyphrase: str = None):
    if keyphrase.lower() == "hari":
        ig = InsultGenerator("Hari")
        response = ig.get_insult()
        args = {"tts": True}
        await ctx.channel.send(response, **args)


@bot.command()
async def list(ctx, what: str = None):
    ...


@bot.command(aliases=("c",))
async def counter(ctx, *, hero_name: str = None):
    print(hero_name)
    if hero_name:
        counters, matched_hero = get_bad_against(hero_name)
        if counters and matched_hero:
            embed = discord.Embed(title=matched_hero, color=0xee7757)
            embed.add_field(name="Bad Against", value=", ".join(counters))
            await ctx.send(embed=embed)


if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))
