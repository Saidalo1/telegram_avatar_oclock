from pyrogram import Client

from config import nickname, bio
from utils import generate_image, set_profile_photo, save_image, set_profile_name_and_bio, delete_all_photos_of_profile


def main():
    # Load configuration values
    from config import API_ID, API_HASH

    # Create the Pyrogram client
    app = Client("Saidalo", api_id=API_ID, api_hash=API_HASH)

    with app:
        # Generate the image
        image = generate_image()

        # Save the image to a temporary file
        image_path = save_image(image)

        # Remove all photos of profile
        delete_all_photos_of_profile(app)

        # Set the profile photo
        set_profile_photo(app, image_path)

        # Set profile name and bio
        set_profile_name_and_bio(app, nickname, bio)


if __name__ == '__main__':
    main()
