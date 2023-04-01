from discord import ComponentInteraction
from discord.ext import commands


class RoleSelection(commands.Cog):


    def __int__(self, bot):
        self.bot = bot


    @commands.Cog.on_select(custom_id='role-selection')
    async def role_selection_dropdown(self, ctx: ComponentInteraction, _):
        user = ctx.author
        selected_roles = ctx.data.values

        # Get the roles from the selected role ids
        roles = [ctx.guild.get_role(int(role_id)) for role_id in selected_roles]

        roles_user_has = [role for role in roles if role in user.roles]
        roles_user_dosent_have = [role for role in roles if role not in user.roles]

        await user.add_roles(*roles_user_dosent_have)
        await user.remove_roles(*roles_user_has)

        roles_added = f'Added roles: { ", ".join(role.name for role in roles_user_dosent_have)}'
        roles_removed = f'Removed roles: {", ".join(role.name for role in roles_user_has)}'

        await ctx.respond(f'{roles_added}\{roles_removed}', hidden=True)



def setup(bot):
    bot.add_cog(RoleSelection(bot))