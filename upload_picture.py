import os
import requests


def download_picture(
    url: str,
    picture_path: str
) -> None:
    os.makedirs("Comics", exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(rf'Comics\{picture_path}', "wb") as file:
        file.write(response.content)
