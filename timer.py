import discord,random,asyncio,os
from datetime import datetime
from discord.ext import commands

send_time='17:00' 							#time is in 24hr format
message_channel_id= 715757990870777906 		#channel ID to send images to


client = discord.Client()

if os.path.isfile('thunderstorm.txt'):
		with open('thunderstorm.txt', "r") as f:
			thunder_list = f.read()
			thunder_list = thunder_list.strip().split("\n")

if os.path.isfile('winds.txt'):
		with open('winds.txt', "r") as f:
			wind_list = f.read()
			wind_list = wind_list.strip().split("\n")

if os.path.isfile('clear.txt'):
		with open('clear.txt', "r") as f:
			clear_list = f.read()
			clear_list = clear_list.strip().split("\n")

if os.path.isfile('clouds.txt'):
		with open('clouds.txt', "r") as f:
			cloud_list = f.read()
			cloud_list = cloud_list.strip().split("\n")

if os.path.isfile('rain.txt'):
		with open('rain.txt', "r") as f:
			rain_list = f.read()
			rain_list = rain_list.strip().split("\n")

if os.path.isfile('special.txt'):
		with open('special.txt', "r") as f:
			special_list = f.read()
			special_list = special_list.strip().split("\n")

@client.event
async def on_ready():
	print(client.user.name)
	print(client.user.id)

async def time_check():
	await client.wait_until_ready()
	message_channel= client.get_channel(message_channel_id)
	while client.is_closed:
		now=datetime.strftime(datetime.now(),'%H:%M')
		if now == send_time:
			roll = random.randint(1, 100)               # Random Roll:
			print("Today's roll is: ", roll)
			if roll < 6:                                # 5% Thunderstorm
				message= random.choice(thunder_list)
			elif roll < 15:                             # 10% Rain
				message= random.choice(rain_list)
			elif roll < 47:                             # 32% Cloudy
				message= random.choice(cloud_list)
			elif roll < 82:                             # 35% Clear
				message= random.choice(clear_list)
			elif roll < 97:                             # 15% Windy
				message= random.choice(wind_list)
			else:                                       # 3% Special
				message= random.choice(special_list)
			await message_channel.send(message)
			time=90
		else:
			time=1
		await asyncio.sleep(time)

client.loop.create_task(time_check())

client.run('NzQ2OTU5NzE1ODE2MTc3Njk0.X0H6cg.f5T5-vQkzoU7hz9BGfvjl1NjvNs')