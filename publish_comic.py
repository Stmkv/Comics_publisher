import requests
import random
import telegram
import os

from dotenv import load_dotenv
from download_picture import download_picture


LAST_COMIC = 2955


def download_comic():
    comics_number = random.randint(1, LAST_COMIC)
    url = f"https://xkcd.com/{comics_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    img_url = response['img']
    comics_comment = response['alt']

    file_path = os.path.join('comics', f'{comics_number}.png')
    download_picture(img_url, file_path)
    return comics_comment, file_path


def publish_comic(bot, chat_id, comments, photo_path):
    bot.send_message(chat_id, comments)
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo)


if __name__ == '__main__':
    try:
        load_dotenv()
        telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
        telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]
        bot = telegram.Bot(token=telegram_bot_token)
        os.makedirs("Comics", exist_ok=True)
        comics_comment, photo_path = download_comic()
        publish_comic(bot, telegram_chat_id, comics_comment, photo_path)
    finally:
        os.remove(photo_path)
