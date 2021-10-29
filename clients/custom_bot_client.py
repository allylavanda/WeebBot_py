from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print("WeebBot is Loading!")

class CustomBotClient(commands.Bot):

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')


client = CustomBotClient('$')
client.run(TOKEN)
