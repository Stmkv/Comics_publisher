import requests
import random
import telegram
import os

from dotenv import load_dotenv
from upload_picture import download_picture


def download_comics():
    comics_number = random.randint(1, 2955)
    url = f"https://xkcd.com/{comics_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    img_url = response['img']
    comics_comment = response['alt']

    file_path = f'comics/{comics_number}.png'
    download_picture(img_url, file_path)
    return comics_comment, file_path


def public_comics(bot, chat_id, comments, photo_path):
    bot.send_message(chat_id, comments)
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo)
    os.remove(photo_path)


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=telegram_bot_token)
    comics_comment, photo_path = download_comics()
    public_comics(bot, telegram_chat_id, comics_comment, photo_path)