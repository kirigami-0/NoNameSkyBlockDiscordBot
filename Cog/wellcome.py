from discord.ext import commands
import common as com

class WellCome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        config = com.Config()
        print("WellCome起動")
        self.channel = self.bot.get_channel(config.getChannelId("wellcome"))
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        message = f"ようこそ{member.mention}さん"
        await self.channel.send(message)


async def setup(bot):
    await bot.add_cog(WellCome(bot))