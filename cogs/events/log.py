"""
	Cog to log all the actions that happen with the bot, in case something goes wrong.
	^^ That's some rhyming up there ;)

	Author: Srikar
"""

from discord.ext import commands

import os
from pathlib import Path
from datetime import date, datetime

def writeLogLine(log_line):
	logs = Path("logs")

	# Making the logs dir if it doesn't exist
	if not os.path.isdir(logs):
		os.mkdir(logs)

	with open(logs / "discord.log", "a") as outFPtr:
		outFPtr.write(log_line)

class log(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# When the bot recieves a command
	# TODO: add message replied to (incase of purge)
	@commands.Cog.listener()
	async def on_command(self, ctx):
		
		log_line = f"{datetime.now()}:COMMAND: Recieved '{ctx.message.content}' from '{ctx.message.author}', in server '{ctx.guild}', in channel '{ctx.channel}'"

		try:
			log_line += f", in category '{ctx.channel.category}'.\n"

		# if the bot is DMed XD
		except AttributeError:
			log_line += f"\n"

		except Exception as e:
			log_line += f"\n{datetime.now()}:ERROR: Something bad happened: '{e}'"

		writeLogLine(log_line)

def setup(bot):
	bot.add_cog(log(bot))