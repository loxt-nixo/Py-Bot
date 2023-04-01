import discord
from discord.ext import commands


class Welcomer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1081531935869911070)

        embed = discord.Embed(title='Willkommen auf Dev Hub!',
                              description=f'Willkommen {member.mention} auf Dev Hub! Wir hoffen du wirst Spaß haben!\n\n'
                                          f'Neue Member Zahl {len(member.guild.members)}!',
                              color=discord.Color.dark_gray())

        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'User ID: {member.id}')

        await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(Welcomer(bot))
