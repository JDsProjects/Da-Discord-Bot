import discord
import re
from discord.ext import commands


async def get_prefix(client, message):
    extras = ["ddb*"]
    comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
    match = comp.match(message.content)
    if match is not None:
        extras.append(match.group(1))
    return commands.when_mentioned_or(*extras)(client, message)


class DaDiscordBot(commands.Bot):
    def __init__(
        self, command_prefix=(get_prefix), help_command=commands.MinimalHelpCommand(), description=None, **options
    ):
        super().__init__(command_prefix, help_command, description, intents=discord.Intents.all(), **options)
