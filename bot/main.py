import discord
import random
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Use .help for a list of commands"))
    print("I am online")

@client.command
async def ping(ctx):
	await ctx.send(f"Pong {round(client.latency)}ms")

@client.command
async def roll(ctx):
	await ctx.send(f"You rolled {random.randint(1,6)}")

@client.command
async def decide(ctx, args*):
	times = 0
	decision = random.randint(1, len(args))
	for i in args:
		times += 1
		if times == decision:
			ctx.send(i)


		


#webhook

client.run(token)