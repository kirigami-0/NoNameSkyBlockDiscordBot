from discord.ext import commands
import common

class WellCome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        config = config()
        self.channel = config.loadChannelId("wellcome")
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.channel.send("ようこそ")


async def setup(bot):
    await bot.add_cog(WellCome(bot))