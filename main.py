import discord, os, random, asyncio, traceback
from discord.ext import commands
import ClientConfig

bot = ClientConfig.client

@bot.listen()
async def on_ready():
  print("Bot is Ready")
  print(f"Logged in as {bot.user}")
  print(f"Id: {bot.user.id}")

async def status_task():
  await bot.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.playing, name="Classic computer games."))
  await asyncio.sleep(40)
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type = discord.ActivityType.watching, name=f"{len(bot.guilds)} servers | {len(bot.users)} users"))
  await asyncio.sleep(40)
 

async def startup():
  await bot.wait_until_ready()
  await status_task()

@bot.event
async def on_error(event, *args, **kwargs):
  more_information = os.sys.exc_info()
  error_wanted = traceback.format_exc()
  traceback.print_exc()
  #print(more_information[0])


bot.loop.create_task(startup())
bot.run(os.environ["TOKEN"])