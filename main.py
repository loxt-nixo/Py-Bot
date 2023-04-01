import logging
import os

import discord
from discord.ext import commands

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

log = logging.getLogger('BOT-MAIN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(),
    intents=intents,
    activity=discord.Activity(type=discord.ActivityType.playing, name='Hello World'),
    status=discord.Status.online,
    sync_commands=True,
    delete_not_existing_commands=True
)

if __name__ == '__main__':
    log.info('starting bot.....')
    cogs = [p.stem for p in Path('cogs').glob('**/*.py') if not p.name.startswith('__')]
    log.info('Loading %d extensions...', len(cogs))

    for cog in cogs:
        bot.load_extension(f'cogs.{cog}')
        log.info('Loaded %s', cog)

    token = os.getenv('BOT_TOKEN')
    bot.run(token)