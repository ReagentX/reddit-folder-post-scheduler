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


if __name__ == "__main__":
    unittest.main()
