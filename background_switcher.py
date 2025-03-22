import discord
from discord.ext import tasks
from PIL import Image
import requests
from io import BytesIO
import os
import random
import platform
import ctypes  # For Windows
import subprocess  # For macOS/Linux
import json

# Load configuration
CONFIG_PATH = "config.json"

if not os.path.exists(CONFIG_PATH):
    print(f"Config file not found! Please ensure {CONFIG_PATH} exists.")
    exit(1)

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

BOT_TOKEN = config.get("BOT_TOKEN")

if not BOT_TOKEN:
    print("Bot token not found in config.json! Please set it before running the bot.")
    exit(1)

BACKGROUND_DIR = "backgrounds"  # Directory to save downloaded images
BACKGROUND_UPDATE_INTERVAL = 10  # In minutes

# Ensure the background directory exists
os.makedirs(BACKGROUND_DIR, exist_ok=True)

# Create the bot instance
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = discord.Client(intents=intents)

# List to store downloaded image file paths
image_files = []

@bot.event
async def on_ready():
    print(f"Connection au bot {bot.user}")
    # Fetch previous messages from all accessible text channels
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                print(f"Channel de recherche des images : {channel.name}")
                async for message in channel.history(limit=100):  # Adjust limit if needed
                    await process_message(message)
            except Exception as e:
                print(f"Erreur de recherche dans le channel : {channel.name}: {e}")
    start_background_task()

@bot.event
async def on_message(message):
    # Process new messages
    await process_message(message)

async def process_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    
    # Check if the message has an attachment
    if message.attachments:
        for attachment in message.attachments:
            # Only process image files
            if attachment.content_type and attachment.content_type.startswith("image/"):
                try:
                    # Download the image
                    response = requests.get(attachment.url)
                    img = Image.open(BytesIO(response.content))
                    
                    # Save the image locally
                    file_name = os.path.join(BACKGROUND_DIR, attachment.filename)
                    img.save(file_name)
                    image_files.append(file_name)
                    print(f"Sauvegarde de l'image : {file_name}")
                except Exception as e:
                    print(f"Echec du chargement de l'image : {e}")



def convert_to_jpg(image_path):
    try:
        with Image.open(image_path) as img:
            jpg_path = os.path.splitext(image_path)[0] + ".jpg"
            img.convert("RGB").save(jpg_path, "JPEG")
            print(f"Conversion du format de : {jpg_path}")
            return jpg_path
    except Exception as e:
        print(f"L'image suivante n'a pas pu être converti : {e}")
        return image_path





@tasks.loop(minutes=BACKGROUND_UPDATE_INTERVAL)
async def update_background():
    if not image_files:
        print("Aucune image disponible.")
        return
    
    # Randomly select an image
    image_file = random.choice(image_files)
    image_file = convert_to_jpg(image_file)
    print(f"Changement du fond d'écran pour : {image_file}")
    set_wallpaper(image_file)


def set_wallpaper(image_path):
    system = platform.system()
    image_path = os.path.abspath(image_path).replace("/", "\\")
    if not os.path.exists(image_path):
        print(f"L'image suivante n'existe pas : {image_path}")
        return


    try:
        if system == "Windows":
            # Windows
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
        elif system == "Linux":
            # Linux (GNOME-based desktops)
            command = f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}"
            os.system(command)
        else:
            print(f"OS non supporté: {system}")
    except Exception as e:
        print(f"Echec du changement de fond d'écran : {e}")

# Start the background task
def start_background_task():
    if not update_background.is_running():
        update_background.start()

# Run the bot
bot.run(BOT_TOKEN)
