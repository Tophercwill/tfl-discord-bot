import discord,random,asyncio,os
from datetime import datetime
from discord.ext import commands

message_channel_id= 715757990870777906 		#channel ID to send images to


client = discord.Client()


@client.event
async def on_ready():
	print(client.user.name)
	print(client.user.id)

	await client.wait_until_ready()
	message_channel= client.get_channel(message_channel_id)
	await message_channel.send("*The day is calm. Perfect. In the far distance, one can see tiny streaks falling to the ground, barely visible behind the bright blue sky.*")

# client.loop.create_task(time_check())

client.run('NzQ2OTU5NzE1ODE2MTc3Njk0.X0H6cg.f5T5-vQkzoU7hz9BGfvjl1NjvNs')