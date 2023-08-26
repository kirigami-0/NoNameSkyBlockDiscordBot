import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
# インテンツを設定
intents = discord.Intents.default()
intents.typing = False

# コマンドを設定
bot = commands.Bot(command_prefix="n.", intents=intents)
# コグの配列を取得
config = json.load(open('config.json', 'r'))
# 起動したらコグを読み込ませる
@bot.event
async def on_ready():
    
    for cog_name in config["cog_name"]:
        await bot.load_extension(f'Cog.{cog_name}')

bot.run(os.getenv("TOKEN"))