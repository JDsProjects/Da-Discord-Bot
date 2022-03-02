import discord, os, random, asyncio, traceback
from discord.ext import commands, tasks
import ClientConfig
from itertools import cycle
import dotenv

bot = ClientConfig.DaDiscordBot()

statuses = ["classic computer games.", "{len(0.guilds)} servers | {len(0.users)} users"]
cycling = cycle(statuses)


@tasks.loop(seconds=40.0)
async def status_task():
    status = next(cycling)
    status = status.format(bot)
    if status.startswith(f"{len(bot.guilds)}"):
        await bot.change_presence(
            status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=status)
        )
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=status)
    )


@bot.event
async def on_ready():
    print("Bot is Ready")
    print(f"Logged in as {bot.user}")
    print(f"Id: {bot.user.id}")
    status_task.start()


@bot.event
async def on_error(event, *args, **kwargs):
    more_information = os.sys.exc_info()
    error_wanted = traceback.format_exc()
    traceback.print_exc()
    # print(more_information[0])


dotenv.load_dotenv()
bot.run(os.environ["TOKEN"])
