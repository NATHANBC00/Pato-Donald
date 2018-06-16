import random
import asyncio
import discord

client = discord.Client()

COR =0x690FC3
msg_id = None
msg_user = None


@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):

    if message.content.lower().startswith('/moeda'):
        escolha = random.randint(1, 2)
        if escolha == 1:
            await client.add_reaction(message, '😀')
        if escolha == 2:
            await client.add_reaction(message, '👑')

    if message.content.lower().startswith("/r6"):
     embed =discord.Embed(
       title="Escolha seu Rank!",
            color=COR,
            description="- Cobre = ♦ \n"
                        "- Bronze  = 🥉 \n"
                        "- Prata  =  🥈 \n"
                        "- Ouro  = 💛 \n"
                        "- Platina  = 🔷 \n"
                        "- Diamnte  = 💎", )

    botmsg = await client.send_message(message.channel,embed=embed )

    await client.add_reaction(botmsg, "♦")
    await client.add_reaction(botmsg, "🥉")
    await client.add_reaction(botmsg, "🥈")
    await client.add_reaction(botmsg, "💛")
    await client.add_reaction(botmsg, "🔷")
    await client.add_reaction(botmsg, "💎")

    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author


@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "♦" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Cobre", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "🥉" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "🥈" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Prata", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "💛" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Ouro", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "🔷" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Platina", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "💎" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Diamante", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "♦" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Cobre", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "🥉" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "🥈" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Prata", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "💛" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Ouro", msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == "🔷" and msg.id == msg_id:
            role = discord.utils.find(lambda r: r.name == "Platina", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")

    if reaction.emoji == "💎" and msg.id == msg_id:
            role = discord.utils.find(lambda r: r.name == "Diamante", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")


client.run('NDU1MzkzMTYxODQ2NDU2MzQw.Df7VlQ.TZNsyNXpEdhScfzC-X9JZ2Jupow')
