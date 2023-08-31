from discord.ext import commands
import common as com
import random

class Lottery(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = com.Config()
        self.omikuji_data = self.config.get_lottery("omikuji")
        print("Lottery起動")
    
    @commands.command()
    async def omikuji(self, ctx):
        value = self.omikuji_data["value"]
        weights = self.omikuji_data["weights"]
        message = f"あなたの運勢は||{random.choices(value, weights=weights)[0]}||"
        await ctx.send(message)


    @commands.command()
    async def set_omikuji(self, ctx, weights=None, value=None):
        """
        おみくじの内容を設定する

        Parameters
        ----------
        ctx : context
            コンテキスト
        weights : str, optional
            確率, by default None
        value : str, optional
            内容, by default None
        """
        message = ""
        try:
            if com.is_empty(weights) and com.is_empty(value):
                # 引数がない場合
                message = "コマンドが不正です"
                await ctx.send(message)
            elif not com.is_empty(weights) and com.is_empty(value):
                # 確率のみある場合
                weights = com.convert_string_to_list(weights, "int")
                print(weights, type(weights))
                if len(weights) == len(self.omikuji_data["value"]):
                    message = "確率を設定しました"
                    self.omikuji_data["weights"] = weights
                    self.config.set_config()
                else:
                    message = '確率数が不正です'
            elif com.is_empty(weights) and not com.is_empty(value):
                value = com.convert_string_to_list(value, "str")
                if len(self.omikuji_data["weights"]) == len(value):
                    message = "内容を設定しました。"
                    self.omikuji_data["value"] = value
                    self.config.set_config()
                else:
                    message = "内容数が不正です。"
            else:
                value = com.convert_string_to_list(value, "str")
                weights = com.convert_string_to_list(weights, "int")
                if len(value) == len(weights):
                    message = "おみくじを設定しました。"
                    self.omikuji_data["value"] = value
                    self.omikuji_data["weights"] = weights
                    self.config.set_config()
                else:
                    message = "不正なエラーです。"
            await ctx.send(message)
        except ValueError:
            await ctx.send("えらー")

async def setup(bot):
    await bot.add_cog(Lottery(bot))