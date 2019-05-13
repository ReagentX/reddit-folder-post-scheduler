import os
import pathlib
import unittest

from imgur_api import upload


class TestImgurMethods(unittest.TestCase):


    def test_upload(self):
        """Upload a sample image to Imgur, make sure we get a link"""
        imgur = upload.ImgurAPI('')
        image_path = pathlib.Path('tests/image.png')
        link = imgur.post_image(image_path, 'test post')
        self.assertIsNotNone(link)


if __name__ == "__main__":
    unittest.main()
