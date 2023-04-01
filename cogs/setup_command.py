import discord
from discord.ext import commands


class SetupCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.slash_command(base_name='setup', name='userinfo', description='Setup the userinfo command')
    async def setup_userinfo_command(self, ctx):
        await ctx.respond('Kilck den Button, um die Userinfo anzuzeigen', components=[
            discord.Button(label='Userinfo', style=discord.ButtonStyle.gray, custom_id='userinfo-btn')
        ])

    @commands.Cog.slash_command(base_name='setup', name='roles', description='Setup the role selection command')
    async def setup_role_selection_command(self, ctx):
        await ctx.respond('Role selection', components=[
            discord.SelectMenu(placeholder='Select your roles', custom_id='role-selection', max_values=3, options=[
                discord.SelectOption(label='New', value='1091773950360567910', emoji='👋'),
                discord.SelectOption(label='Long', value='1091773974888857732', emoji='😋'),
                discord.SelectOption(label='old', value='1091774000088219649', emoji='🧓'),
            ])
        ])


def setup(bot):
    bot.add_cog(SetupCommand(bot))