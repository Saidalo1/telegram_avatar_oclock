import datetime

from PIL import Image, ImageDraw, ImageFont

from config import WIDTH, HEIGHT, BACKGROUND_COLOR, FONT_SIZE, TEXT_COLOR

# Load font when start script
font = ImageFont.truetype('arial.ttf', FONT_SIZE)


def generate_image():
    # Create an image with a black background
    image = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)

    # Get the current time in Tashkent
    tz_offset = datetime.timedelta(hours=5)  # Timezone offset
    time_tashkent = datetime.datetime.utcnow() + tz_offset
    formatted_time = f" You will see this image at \n                {time_tashkent.strftime('%H:%M')}"

    # Create a Draw object for drawing on the image
    draw = ImageDraw.Draw(image)

    # Calculate the coordinates of the text for center alignment on the image
    text_width, text_height = draw.textsize(formatted_time, font=font)
    text_x = (WIDTH - text_width) // 2
    text_y = (HEIGHT - text_height) // 2

    # Draw the text in green color on the image
    draw.text((text_x, text_y), formatted_time, font=font, fill=TEXT_COLOR)

    return image


def set_profile_photo(api_client, image):
    # Set the profile photo using Pyrogram API
    api_client.set_profile_photo(photo=image)


def save_image(image):
    temp_path = "avatar_image.jpg"
    image.save(temp_path, format='JPEG')  # Use JPEG format for optimization
    return temp_path
