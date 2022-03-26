import discord, os, random, asyncio, traceback, re
from discord.ext import commands
import dotenv


async def get_prefix(client, message):
    extras = ["ddb*"]
    comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
    match = comp.match(message.content)
    if match is not None:
        extras.append(match.group(1))
    return commands.when_mentioned_or(*extras)(client, message)


async def startup(self):
    await self.wait_until_ready()
    await status_task()


async def status_task(self):
    await self.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(type=discord.ActivityType.playing, name="Classic computer games."),
    )
    await asyncio.sleep(40)
    await self.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"{len(self.guilds)} servers | {len(self.users)} users"
        ),
    )
    await asyncio.sleep(40)


class DaDiscordBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self):
        self.loop.create_task(startup(self))


bot = DaDiscordBot(command_prefix=(get_prefix), intents=discord.Intents.all())


@bot.listen()
async def on_ready():
    print("Bot is Ready")
    print(f"Logged in as {bot.user}")
    print(f"Id: {bot.user.id}")


@bot.event
async def on_error(event, *args, **kwargs):
    more_information = os.sys.exc_info()
    error_wanted = traceback.format_exc()
    traceback.print_exc()
    # print(more_information[0])


dotenv.load_dotenv()
bot.run(os.environ["TOKEN"])
