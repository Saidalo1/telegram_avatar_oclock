import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Pyrogram API credentials
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# Image generation settings
WIDTH = 640
HEIGHT = 640
BACKGROUND_COLOR = (0, 0, 0)  # Black background color
FONT_SIZE = 54
TEXT_COLOR = (0, 255, 0)  # Green text color
