import discord
import requests
import json
import random
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

keep_alive()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


def get_meme():
    response = requests.get('https://api.imgflip.com/get_memes')

    if response.status_code != 200:
        return "No se pudo obtener un meme en este momento. 😢"

    json_data = response.json()

    # Elegir un meme aleatorio de la lista de memes
    memes = json_data["data"]["memes"]
    meme = random.choice(memes)

    return meme["url"]  # Retorna solo la URL de la imagen


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Evitar que el bot responda a sus propios mensajes
        if message.author == self.user:
            return

        if message.content.startswith('$meme'):
            meme_url = get_meme()
            await message.channel.send(meme_url)


# Configuración de intents
intents = discord.Intents.default()
intents.message_content = True

# Crear instancia del bot con intents
client = MyClient(intents=intents)
client.run(TOKEN)  # Replace with your own token.
