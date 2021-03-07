import discord
from discord.ext import commands
import os

import random

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    print(f"{member} has joined {member.guild}")

@client.event
async def on_member_remove(member):
    print(f"{member} has left {member.guild}")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
async def flip(ctx):
    side = random.randint(1,2)
    
    if  side == 1:
        await ctx.send("Heads!")
    
    elif side == 2:
        await  ctx.send("Tails!")

@client.command()
async def decide(ctx, option1="yes", option2="no"):
        choice = random.randint(1,2)

        if choice == 1:
            await ctx.send(f"I Choose: {option1}")
        
        elif choice == 2:
            await ctx.send(f"I Choose: {option2}")

@client.command(aliases = ["8ball"])
async def _8ball(ctx, *args):
    eightball = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]

    await ctx.send(eightball[random.randint(0,19)])

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def echo(ctx, title, content):
    await ctx.send(embed = discord.Embed(title = title, description = content, color = 0xffae00))
    
client.run(os.getenv("DISCORD_BOT_TOKEN"))