# discord_message_replacer
Python script for a Discord Bot, creation assisted by ChatGPT. You can easily change what you want in the config.json

This is just a drag and drop wherever you want to run the bot. Make sure you already have the Discord module with Pip.
Make sure to put *your* token in the config.json! - The urls in there are the current ones I've been using, feel free to replace as you see fit.

What the bot will do, is that as soon as it detects a message that has any of the listed urls in config.json, it will delete that message, and send a new one which is the exact same one with the original author's discord username, and the url from the message gets replaced.

You could apply this functionaly for any part of a message, I've made this for a private server so we can send appropriately embed tweets in messages. Modify and change to your needs!

Here's the bot with this script in action:
![71062ae064c0815416fa3bf544ea7823](https://github.com/p8wer/discord_message_replacer/assets/31834469/0c44087c-42b8-44d5-8ca8-c60f7946ea7c)
