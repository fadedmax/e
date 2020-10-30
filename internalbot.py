import discord
from discord.utils import get
import random
import datetime
from discord.ext.commands import ConversionError
from discord.ext import commands

client = commands.Bot(command_prefix="")
client.remove_command("help")

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers | help."))
	print("Now Sending Data")
	print("...")
	print("...")
	print("...")
	print("...")
	print("commands now accesible!")

@client.command(aliases=['hi', 'Hi', 'HI', 'hI', 'Hello', 'Hiya', 'hello', 'hiya', 'Yo', 'yo'])
async def h(ctx):       
	await ctx.send("Hello dude!")
	
async def is_owner(ctx):

    return ctx.author.id == 746807014658801704 
    
@client.command(aliases=['r'])
@commands.check(is_owner)
async def raid(ctx):
	await ctx.send("raid.exe running")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("@everyone")
	await ctx.send("Raiding complete")
	
@client.command()
async def slap(ctx, member : discord.Member):
	choices = ['https://giphy.com/gifs/angry-fight-family-guy-uqSU9IEYEKAbS', 'https://giphy.com/gifs/pokemon-pikachu-Qv7WFppXtkqkM', 'https://giphy.com/gifs/angry-fight-family-guy-uqSU9IEYEKAbS']
	slap = random.choice(choices)
	await ctx.send(slap)
	
@client.command(aliases=['E', 'EE', 'ee'])
async def e(ctx):
	choices = ['E', 'EE', 'e', 'ee', 'no u', 'HAHA no']
	e = random.choice(choices)
	await ctx.send(e)
	
@client.command(aliases=['<@748488992021938226>'])
async def ping(ctx):
	await ctx.send("Type `help` for more info.")
	
@client.command(aliases=["sc"])
async def servercount(ctx):
	await ctx.send(f"The bot is in {len(client.guilds)} servers!")
	
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
	await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member, *,reason="No Reason Provided"):
  await member.kick(reason=reason)
  await member.send("You have been kicked because:+reason")
  await ctx.send(member.mention + "was kicked")
	
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member, *,reason="No Reason Provided"):
	member.send("You have been banned, because:+reason")
	await member.ban(reason=reason)
	await ctx.send(member.mention + " has been banned.")
	
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *,member):
	banned_users = await ctx.guild.bans()
	member_name, member_disc = member.split('#')
	
	for banned_entry in banned_users:
		user = banned_entry.user
		
		if(user.name, user.discriminator)==(member_name,member_disc):
			
			await ctx.guild.unban(user)
			await ctx.send(member_name +" has been unnbaned!")
			
@client.command()
async def coinflip(ctx):
	choices = ["Heads", "Tales"]
	rancoin = random.choice(choices)
	await ctx.send(rancoin)

@client.command(aliases=['8ball'])
async def _8ball(ctx):
	choices = ["No", "Yes", "Nope", "Its A Certain", "Yeah", "dont know", "try again later", "nu", "not gonna answer, play among us noob", "My Magic Ball says yes", "my magic ball says no", "Most Likely Yes", "Most likely yes", "cant tell you now", "Hey weeb, go watch anime", "ew a gamer get a life", "Very doubtful", "Cannot predict now"]
	ball = random.choice(choices)
	await ctx.send(ball)
	
@client.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, msg):
	await ctx.message.delete()
	await ctx.send("{}" .format(msg))
	
@client.command()
async def help(ctx):
	embed = discord.Embed(
	colour=discord.Colour.blue(),
	title="Command Help"
	)
	
	embed.set_author(name="", icon_url="")
	embed.add_field(name="ban", value="Ban the member you mention.")
	embed.add_field(name="unban", value="Unban the user you want like this: Random#0400.")
	embed.add_field(name="kick", value="kick the member you mention.")
	embed.add_field(name="coinflip", value="Flip a coin.")
	embed.add_field(name="8ball", value="Ask it a question and itll answer.")
	embed.add_field(name="say", value="Make the bot say something, you need manage messages perms.")
	embed.add_field(name="lul", value="Make the bot send a funny image.")
	embed.add_field(name="invite", value="Get the bot invite..")
	embed.add_field(name="userinfo", value="Get the information of a user")
	embed.add_field(name="serverinfo", value="Get the informtion of the server!")
	embed.add_field(name="avatar", value="Get avatar of a user")
	embed.add_field(name="servercount", value="Get the amount of servers the bot is in!")
	embed.add_field(name="slap", value="Slap a user!!")
	embed.set_footer(text="If you need help, type help!")
	
	await ctx.send(embed=embed)
	
@client.command()
async def invite(ctx):
	invite = discord.Embed(
	colour=discord.Colour.orange(),
	title="Invite"
	)
	
	invite.set_author(name="", icon_url="")
	invite.add_field(name="Bot Invite:", value="https://discord.com/api/oauth2/authorize?client_id=748488992021938226&permissions=8&scope=bot")
	
	await ctx.send(embed=invite)
	
@client.command()
async def lul(ctx):
	await ctx.send("https://media.discordapp.net/attachments/768908707765289044/770685112378589204/download_20.jpeg?width=100&height=100")
	
@client.command(aliases=['userinfo'])
async def whois(ctx, member : discord.Member):
	roles = [role for role in member.roles]
	who = discord.Embed(title = member.name, color = discord.Colour.red())
	who.add_field(name = "ID", value = member.id, inline = True)
	who.add_field(name = "Created At", value = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = True)
	who.add_field(name = "Joined At", value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = True)
	who.add_field(name=f"Top Role", value = member.top_role.mention)
	who.add_field(name=f"Roles ({len(roles)})", value = " ".join([role.mention for role in roles]))
	who.add_field(name="Bot?", value=member.bot)
	who.set_thumbnail(url = member.avatar_url)
	who.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
	await ctx.send(embed=who)

@client.command(aliases=['Avatar', 'av'])

async def avatar(ctx, user: discord.Member):

    mbed = discord.Embed(

        color = discord.Color(0xffff),

        title=f"{user}"

    )

    mbed.set_image(url=f"{user.avatar_url}")

    await ctx.send(embed=mbed)



@client.command(aliases=['ServerInfo'])

async def serverinfo(ctx, guild: discord.Guild = None):

    sbed = discord.Embed(

        color=discord.Color(0xffff),

        title=f"{ctx.guild.name}"

    )

    sbed.set_thumbnail(url=f"{ctx.guild.icon_url}")

    sbed.add_field(name='Region', value=f"{ctx.guild.region}") 
   
    sbed.add_field(name='Member Count', value=f"{ctx.guild.member_count}")

    sbed.set_footer(icon_url=f"{ctx.guild.icon_url}", text=f"Guild ID: {ctx.guild.id}")

    await ctx.send(embed=sbed)

client.run("NzQ4NDg4OTkyMDIxOTM4MjI2.X0eKsQ.EdrqfyFPRNpLrUe--jTDg2POeB8")
