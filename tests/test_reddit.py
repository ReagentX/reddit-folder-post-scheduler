import os
import pathlib
import unittest

from reddit_api import submit


class TestRedditMethods(unittest.TestCase):

    def test_submit(self):
        """Submit a test post and delete"""
        submission = submit.post('test', 'title test', 'https://test.com')
        self.assertIsNotNone(submission)
        submission.delete()

    def test_submit_video(self):
        """Submit a test video and delete"""
        video = pathlib.Path('tests/test.mp4')
        thumb = submit.get_first_frame(video)
        submission = submit.post_video('test', 'title test', video, thumb)
        self.assertIsNotNone(submission)
        print(submission.permalink)
        # Cleanup
        submission.delete()
        os.remove(thumb)


if __name__ == "__main__":
    unittest.main()
