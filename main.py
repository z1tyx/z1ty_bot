import logging
import discord
import os

from dotenv import load_dotenv

load_dotenv('.env')

TOKEN = os.getenv("BOT_TOKEN")

client = discord.Client()

client.run(TOKEN)
