from pyrogram import Client

from utils import generate_image, set_profile_photo, save_image


def main():
    # Load configuration values
    from config import API_ID, API_HASH

    # Create the Pyrogram client
    app = Client("my_bot", api_id=API_ID, api_hash=API_HASH)

    with app:
        # Generate the image
        image = generate_image()

        # Save the image to a temporary file
        image_path = save_image(image)

        # Set the profile photo
        set_profile_photo(app, image_path)


if __name__ == '__main__':
    main()
