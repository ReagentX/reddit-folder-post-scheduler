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
        return [filename for filename in os.listdir(dir) if filename not in self.used]

    
    def create_folder(self, name) -> None:
        '''Create user folder to download files into'''
        if not os.path.exists(name):
            os.makedirs(name)


    def get_or_create_log(self) -> list:
        self.create_folder('log')
        used = set()
        with open(self.log_root / 'log.txt', 'r') as f:
            for line in f.readlines():
                used.add(line.strip())
        return used


    def get_random_image(self) -> str:
        choice = random.choice(self.files)
        with open(self.log_root / 'log.txt', 'a') as f:
            print(f'Logging {choice}')
            f.write(f'{choice}\n')
        return choice

    
    def make_posts(self) -> None:
        image = self.get_random_image()
        path = self.root / image
        title = image.split('.')[0]

        # Upload to Imgur
        url = self.imgur.post_image(path, title)

        # Submit to Reddit
        for sub in self.subreddits:
            submission = submit.post(sub, title, url)
            print(f'https://old.reddit.com{submission.permalink}')

        print('Done!')

    def __repr__(self):
        return f'Scheduler object\n{len(self.files)} choices\n{len(self.subreddits)} subreddits'
