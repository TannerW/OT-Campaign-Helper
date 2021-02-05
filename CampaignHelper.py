import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

import psycopg2


load_dotenv()
TOKEN = os.getenv('TOKEN')


# client = discord.Client()

bot = commands.Bot(command_prefix='%')



# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="D&D 5e | &help")); 

@bot.command(name='99', help='test')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='listNPCs', help='lists all NPCs')
async def listNPCs(ctx):
    conn = psycopg2.connect(database="ot-campaign-helper", user = "ot-campaign-helper", password = "password", host = "192.168.1.110", port = "5433")
    cur = conn.cursor()

    cur.execute("SELECT * from npcs")
    rows = cur.fetchall()

    response = ""

    for row in rows:
        response = response +"**"+ row[1]+"** - " + row[7] + "\n"

    conn.close()
    await ctx.send(response)

@bot.command(name='addNPC', help='add an NPC')
async def addNPC(ctx):
    conn = psycopg2.connect(database="ot-campaign-helper", user = "ot-campaign-helper", password = "password", host = "192.168.1.110", port = "5433")
    cur = conn.cursor()
    
    command = "INSERT INTO npcs (name, occupation, class, meetingLocation, faction, friendliness, notes, race) VALUES ("

    def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

    msgsToDelete = []

    msg = await ctx.send(f"NPC's name:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"NPC's occupation:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"NPC's class:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"NPC's location where met:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"NPC's faction:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"NPC's friendliness:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"NPC's notes:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "',"

    msg = await ctx.send(f"NPC's race:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "'"

    command = command + ")"
    cur.execute(command)
    conn.commit()

    # msgs = await ctx.channel.history(limit=40).flatten()

    # count = 8
    # for msg in msgs:
    #     if (msg.author.id == ctx.author.id and count > 0):
    #         await msg.delete()
    #         count = count - 1

    #await ctx.channel.purge(limit=8, check=lambda x: (x.author.id == ctx.author.id))

    response = "NPC added!"
        
    conn.close()
    await ctx.send(command)
    await ctx.send(response)
    for msg in msgsToDelete:
        await msg.delete()


@bot.command(name='addObj', help='add an objective')
async def addObj(ctx):
    conn = psycopg2.connect(database="ot-campaign-helper", user = "ot-campaign-helper", password = "password", host = "192.168.1.110", port = "5433")
    cur = conn.cursor()
    
    command = "INSERT INTO objectives (name, objective_type, description, patron_npc, status, starting_area, target_areas) VALUES ("

    def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

    msgsToDelete = []

    msg = await ctx.send(f"Give the objective a brief name:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"What category of objective is it (Quest, Rumor, Obligation):")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"A description of the objective:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"The ID of the patron NPC:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"What is the status of the objective (ongoing, completed, failed, other):")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"What is the name of the area/town where you got this objective:")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "', "

    msg = await ctx.send(f"What other areas does this objective involve? (such as where the objective will take you):")
    msgsToDelete.append(msg)
    msg = await bot.wait_for('message', check=check)
    msgsToDelete.append(msg)
    command = command + "'" + msg.content.replace('\'', '\'\'') + "'"

    # msg = await ctx.send(f"IDs of related objectives:")
    # msgsToDelete.append(msg)
    # msg = await bot.wait_for('message', check=check)
    # msgsToDelete.append(msg)
    # command = command + "'" + msg.content.replace('\'', '\'\'') + "'"

    command = command + ")"
    cur.execute(command)
    conn.commit()

    # msgs = await ctx.channel.history(limit=40).flatten()

    # count = 8
    # for msg in msgs:
    #     if (msg.author.id == ctx.author.id and count > 0):
    #         await msg.delete()
    #         count = count - 1

    #await ctx.channel.purge(limit=8, check=lambda x: (x.author.id == ctx.author.id))

    response = "Objective added!"
        
    conn.close()
    await ctx.send(command)
    await ctx.send(response)
    for msg in msgsToDelete:
        await msg.delete()

# @bot.event
# async def on_message(message):
#     channels = ["test"]
#     valid_users = ["Tanner#1753"]

#     if str(message.channel) in channels and str(message.author) in valid_users:
#         await message.channel.send('👋') 

bot.run(TOKEN)

#SELECT * FROM npcs where npc_id = (SELECT patron_npc FROM objectives WHERE obj_id = 5)