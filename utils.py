from datetime import date, timedelta, datetime

from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client

from config import WIDTH, HEIGHT, BACKGROUND_COLOR, FONT_SIZE, TEXT_COLOR

# Load font when start script
font_path = "/root/scripts/telegram_avatar_oclock/fonts/arial.ttf"
font = ImageFont.truetype(font_path, FONT_SIZE)


def time_tashkent() -> date:
    """
    Get the current time in Tashkent
    :return:
    """
    tz_offset = timedelta(hours=5)  # Timezone offset
    return datetime.utcnow() + tz_offset


def generate_image() -> Image:
    # Create an image with a black background
    image = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)

    formatted_time = f" You will see this image at \n                {time_tashkent().strftime('%H:%M')}"

    # Create a Draw object for drawing on the image
    draw = ImageDraw.Draw(image)

    # Calculate the coordinates of the text for center alignment on the image
    text_width, text_height = draw.textsize(formatted_time, font=font)
    text_x = (WIDTH - text_width) // 2
    text_y = (HEIGHT - text_height) // 2

    # Draw the text in green color on the image
    draw.text((text_x, text_y), formatted_time, font=font, fill=TEXT_COLOR)

    return image


async def set_profile_photo(api_client: Client, image):
    # Set the profile photo using Pyrogram API
    await api_client.set_profile_photo(photo=image)


def save_image(image) -> str:
    temp_path = "avatar_image.jpg"
    image.save(temp_path, format='JPEG')  # Use JPEG format for optimization
    return temp_path


async def set_profile_name_and_bio(api_client: Client, nickname: str, bio: str):
    # Configure profile's nickname and bio
    nickname += f" | ⏰{time_tashkent().strftime('%H:%M')}"
    bio += f" | ⏰{time_tashkent().strftime('%H:%M')}"

    # Update profile
    await api_client.update_profile(nickname, bio=bio)


async def delete_all_photos_of_profile(api_client: Client):
    # Get all photo of profile
    photos_count = await api_client.get_chat_photos_count('me')
    photos = api_client.get_chat_photos('me', photos_count)

    # Delete all photos
    async for photo in photos:
        await api_client.delete_profile_photos(photo.file_id)
