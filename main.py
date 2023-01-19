import discord

bot = discord.Bot()

@bot.command()
async def slashCommandName( #Write your slash command's name
  ctx,
 # option: discord.Option(discord.SlashCommandOptionType.string) // This is if you want to add arguments / options to your commands

):
  # Your command here
  
 
bot.run("TOKEN")
