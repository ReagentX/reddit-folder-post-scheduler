import json
import requests

API_ROOT = 'https://api.imgur.com/3/'

class ImgurAPI():
    def __init__(self, client_id):
        self.headers = {
            'Authorization': f'Client-ID {client_id}'
        }


    def post_image(self, image, title):
        body = {
            'image': image,
            'type': 'file',
            'name': title,
            'title': title,
            'description': '',
            'disable_audio': 1
        }

        url = f'{API_ROOT}/upload'
        response = requests.post(url, data=body, headers=self.headers)
        print(response)
        if response.json():
            return response.json()['data']['link']
        else:
            return None