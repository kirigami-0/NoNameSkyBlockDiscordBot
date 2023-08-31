import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
# インテンツを設定
intents = discord.Intents.default()
intents.typing = False
intents.message_content = True
intents.members = True

# コマンドを設定
bot = commands.Bot(command_prefix="n.", intents=intents)

# コグの配列を取得
cogs = os.listdir("./Cog")
@bot.event
async def on_ready():
    """
    起動処理
    """
    print("bot起動")
    for cog_name in cogs:
        if cog_name.endswith(".py"):
            print(f"Cog.{cog_name[:-3]}")
            await bot.load_extension(f"Cog.{cog_name[:-3]}")

bot.run(os.getenv("TOKEN"))