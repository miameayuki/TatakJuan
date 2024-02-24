from typing import Optional
import discord
from discord.ext import commands
from dotenv import load_dotenv
import discord.ui
import os

load_dotenv()

intents = discord.Intents.all()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix= '.', intents = intents, help_command=None)

class  Verification(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verify", custom_id="Verify", style=discord.ButtonStyle.success)
    async def verify(self, interaction: discord.Interaction, button: discord.Button):
        role = 1205520956945207326
        user = interaction.user
        if role not in [y.id for y in user.roles]:
            await user.add_roles(user.guild.get_role(role))
            await user.send("**Welcome to TatakJuan\n\n**" "This is to confirm that you are already verified in the Discord server. Please refrain from interacting with this message or any other DM unless you personally know the sender, as they could potentially be a scam. Remember, team members of TatakJuan will never DM you. If you have any concerns or require assistance, please reach out to us directly through our official channels.")
            await interaction.response.send_message("Verification is complete!", ephemeral=True)

@bot.event
async def on_ready():
    print('System rebooted.')
    bot.add_view(Verification())

@bot.command()
async def initialize(ctx):
    desc1 = ("**Maligayang pagdating sa aming komunidad kabayan!**\n"
             "- Welcome to our community!*\n\n"
             "**Para magkaroon ng pahintulot sa lahat ng aming tampok na dako, pindutin ang Verify na button sa ibaba.**\n"
             "- To have permission in all our channels, press the Verify button below.*\n\n"
             "**Kapag ika'y naberipika na, magagawa mong ganap na makisali sa aming komunidad at makilahok sa lahat ng aming mga kaganapan at aktibidad.**\n"
             "- Once you're verified, you'll be able to fully engage with our community and participate in all of our events and activities.*")
    embed = discord.Embed(title = "Verification", description=(desc1))
    await ctx.send(embed = embed, view = Verification())

bot.run(TOKEN)