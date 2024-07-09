import os
import requests


def download_picture(
    url: str,
    picture_path: str
) -> None:
    response = requests.get(url)
    response.raise_for_status()

    with open(picture_path, 'wb') as file:
        file.write(response.content)
