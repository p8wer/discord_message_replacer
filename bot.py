import discord
import json

# Load the configuration data from the config.json file
with open('config.json', 'r') as f:
    config = json.load(f)

#intents = discord.Intents(messages=True)
client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')
    await client.change_presence(activity=discord.Game(name="with ChatGPT"))

@client.event
async def on_message(message):
    print('Message received')
    for old_url, new_url in config.get("replacements", {}).items():
        if old_url in message.content:
            old_message = message.content
            new_message = old_message.replace(old_url, new_url)
            author_name = message.author.name
            custom_text = '**' + author_name + '** 💬' + '\n'
            await message.channel.send(custom_text + new_message)
            await message.delete()

client.run(config['token'])
