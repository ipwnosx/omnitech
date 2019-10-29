from discord.ext import commands  # python3.7 -m pip install discord.py
import discord  # python3.7 -m pip install discord.py
import random

help_title = ""
url = ""
colour = 999
help_fields = [
    {"name": "phone no.", "value": "999", "inline": False},
    {"name": "email", "value": "k@k.com", "inline": False}
]
maintainer = ""
img_url = ""
logo_url = ""
types = {
    "nord": "nord.txt",
    "hulu": "Hulu_Premium.txt"
}
types_keys = list(types.keys())


class Generator(commands.Cog):
    def __init__(self, bot):
        self.Bot = bot
        self.Bot.bot.remove_command('help')
        print("ACCOUNT GENERATOR >> Loaded.")

    @commands.guild_only()
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title=help_title, description=help_title, url=url, colour=colour)
        for field in help_fields:
            embed.add_field(name=field["name"], value=field["value"], inline=field["inline"])
        embed.set_footer(text=f"Maintained by {maintainer}", icon_url=img_url)
        embed.set_thumbnail(url=logo_url)
        await ctx.channel.send(embed=embed)

    @commands.cooldown(1, 8)
    @commands.guild_only()
    @commands.command()
    async def gen(self, ctx, type=None):
        if not type:
            await ctx.channel.send("Please specify a type of account to generate.")
        elif type not in types_keys:
            await ctx.channel.send("This is an invalid type!")
        else:
            with open(types[type], "r") as fp:
                data = fp.readlines()
                if len(data) == 0:
                    await ctx.channel.send(f"There are no {type} accounts available!")
                    return
                num = random.randint(0, len(data))
                await ctx.channel.send(f"Your {type} account is {data[num]}")

    @commands.guild_only()
    @commands.command()
    async def types(self, ctx):
        con = ""
        for x in range(len(types_keys)):
            if x == len(types_keys)-1:
                con = con + str(types_keys[x]) + "."
            else:
                con = con + str(types_keys[x]) + ", "
        await ctx.channel.send(f"The available types are {con}")
