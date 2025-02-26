import discord
from Secrets import *
from AutoTyper import *

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)


CHANNEL_ID = Secrets.TEST_SERVER_CHANNEL_ID
GUILD_ID = Secrets.SERVER_ID

# Class instance
auto_typer = AutoTyper(bot)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.sync_commands()
    print(f"Commands synced!")


@bot.slash_command(guild_ids=[GUILD_ID], name="start_bot", description="Starts the auto-typer in this server.")
async def start_bot(ctx):
    auto_typer.start(ctx.guild.id, ctx.channel.id)
    await ctx.respond(f"AutoTyper started in {ctx.channel.mention}.")

@bot.slash_command(guild_ids=[GUILD_ID], name="stop_bot", description="Stops the auto-typer in this server.")
async def stop_bot(ctx):
    auto_typer.stop(ctx.guild.id)
    await ctx.respond(f"AutoTyper stopped in this server.")

@bot.slash_command(guild_ids=[GUILD_ID], name="set_message", description="Changes the auto-typer message.")
async def set_message(ctx, new_message: discord.Option(str, description="The new message to type")):
    auto_typer.setMessage(ctx.guild.id, new_message)
    await ctx.respond(f"AutoTyper message updated to: `{new_message}`")

@bot.slash_command(guild_ids=[GUILD_ID], name="set_interval", description="Set the message interval for the bot")
async def set_interval(ctx, new_interval: discord.Option(float, description="New interval in seconds")):
    auto_typer.setInterval(ctx.guild.id, new_interval)
    await ctx.respond(f"AutoTyper interval updated to {new_interval} seconds.")

@bot.slash_command(guild_ids=[GUILD_ID], name="help", description="Provides help menu")
async def help_menu(ctx):
    embed = discord.Embed(
        title="🤖 AutoTyper Help Menu",
        description="Here are the available commands for AutoTyper:",
        color=discord.Color.blue()
    )

    embed.add_field(name="/start_bot", value="Starts the AutoTyper in the current channel.", inline=False)
    embed.add_field(name="/stop_bot", value="Stops the AutoTyper in the current channel.", inline=False)
    embed.add_field(name="/set_message <message>", value="Sets a new message for AutoTyper.", inline=False)
    embed.add_field(name="/set_interval <seconds>", value="Sets the interval for AutoTyper in seconds.", inline=False)
    embed.add_field(name="/help", value="Displays this help menu.", inline=False)


    await ctx.respond(embed=embed)



if __name__ == "__main__":
    bot.run(Secrets.BOT_TOKEN)