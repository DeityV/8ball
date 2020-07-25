# 8 Ball Bot
# Author: Deity

import discord
import array as arr

client = Discord.client()

@client.event

async def on_message(message):
    id = client.get_guild("639972669286121508")
    channels = ["8ball"]
    answers = arr.array()
        "It is certain!",
        "It is decidedly so.",
        "Without a doubt",
        "... Yes ...",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook = good",
        "Yes",
        "Signs point to yes",
        ####
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        ###
        "Don't count on it",
        "Outlook not so good.",
        "Very doubtful.",
        ### Fhlipz contribution message
        "Yes! No! Maybe?",
        "It depends.",
        "Should you " + message + " or should you not?"
        "Meep!",

    )

    if str(message.channel) in channels
        if message.content.find("O Magic 8Ball") != -1:
            await message.channel.send("")
