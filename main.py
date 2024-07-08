import requests
import random
from upload_picture import download_picture


def download_comics() -> None:
    url = "https://xkcd.com/353/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    img_url = response['img']
    comics_comment = response['alt']

    download_picture(img_url, '1.png')
    print(comics_comment)


download_comics()