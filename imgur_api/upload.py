import json
import pathlib

import requests



class ImgurAPI():
    def __init__(self, client_id):
        self.headers = {
            'Authorization': f'Client-ID {client_id}'
        }
        self.log_root = pathlib.Path('log')
        self.api_root = 'https://api.imgur.com/3/'


    def post_image(self, image_path: pathlib.Path, title: str) -> str:
        """POSTs an image file to the Imgur API; returns the upload's URL"""
        with open(image_path, 'rb') as f:
            image = f.read()
        body = {
            'image': image,
            'type': 'file',
            'name': title,
            'title': title,
            'description': '',
            'disable_audio': 1
        }

        url = f'{self.api_root}/upload'
        response = requests.post(url, data=body, headers=self.headers)
        if response.json():
            link = response.json()['data']['link']
            deletehash = response.json()['data']['deletehash']

            # Log link and deletehash so we can remove anonymous uploads
            with open(self.log_root / 'image.txt', 'a') as f:
                print(f'Logging {link}')
                f.write(f'{link}|{deletehash}\n')
            return link, deletehash
        else:
            return None


    def delete_image(self, deletehash: str):
        url = f'{self.api_root}/image/{deletehash}'
        response = requests.delete(url, headers=self.headers)
        return response if response else None