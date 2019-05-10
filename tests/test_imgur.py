import os
import pathlib
import unittest
from imgur_api import upload


class TestImgurMethods(unittest.TestCase):

    imgur = upload.ImgurAPI('')
    base_path = pathlib.Path('tests/')


    def test_upload(self):
        with open(f'{self.base_path}/image.png', "rb") as f:
            image = f.read()
        link = self.imgur.post_image(image, 'test post')
        self.assertIsNotNone(link)


if __name__ == "__main__":
    unittest.main()
