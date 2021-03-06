import os
import pathlib
import random

from imgur_api import upload
from reddit_api import submit


class Scheduler():
    def __init__(self, dir: pathlib.Path, subreddits: list, imgur_key: str):
        self.root = dir
        self.log_root = pathlib.Path('log/')
        self.used = self.get_or_create_log()
        self.files = self.get_files_in_dir(dir)
        if not self.files:
            raise ValueError('No unused files!')
        self.subreddits = subreddits
        self.imgur = upload.ImgurAPI(imgur_key)


    def get_files_in_dir(self, dir: pathlib.Path) -> list:
        """Returns a list of unused files, i.e. files not named in `log.txt`"""
        return [filename for filename in os.listdir(dir) if filename not in self.used]

    
    def create_folder(self, name) -> None:
        """Create folder if folder does not exist"""
        if not os.path.exists(name):
            os.makedirs(name)


    def get_or_create_log(self) -> set:
        """Gets the data from `log.txt` (or creates it if the file does not exist"""
        self.create_folder('log')
        used = set()
        with open(self.log_root / 'log.txt', 'r') as f:
            for line in f.readlines():
                used.add(line.strip())
        return used


    def get_random_image(self) -> str:
        """Chooses a random file from the files list, logs it, and returns the name"""
        choice = random.choice(self.files)
        with open(self.log_root / 'log.txt', 'a') as f:
            print(f'Logging {choice}')
            f.write(f'{choice}\n')
        return choice

    
    def make_posts(self) -> None:
        """Get a random unused image, upload to Imgur, post to Reddit"""
        image = self.get_random_image()
        path = self.root / image
        title = image.split('.')[0]

        # Upload to Imgur, get the URL
        if image.endswith('png'):
            url, deletehash = self.imgur.post_image(path, title)
            # Submit URL to Reddit
            for sub in self.subreddits:
                submission = submit.post(sub, title, url)
                print(f'https://old.reddit.com{submission.permalink}', file=open(self.log_root / 'links.txt', 'a'))
        else:
            thumb = submit.get_first_frame(path)
            for sub in self.subreddits:
                submission = submit.post_video(sub, title, path)
                print(f'https://old.reddit.com{submission.permalink}', file=open(self.log_root / 'links.txt', 'a'))
            os.remove(thumb)

        print('Done!')

    def __repr__(self):
        return f'Scheduler object\n{len(self.files)} choices\n{len(self.subreddits)} subreddits'
