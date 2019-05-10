import os
import pathlib
import unittest
from imgur_api import upload


class TestImgurMethods(unittest.TestCase):

    imgur = upload.ImgurAPI('')


    def test_upload(self):
        image_path = pathlib.Path('tests/image.png')
        link = self.imgur.post_image(image_path, 'test post')
        self.assertIsNotNone(link)


if __name__ == "__main__":
    unittest.main()
